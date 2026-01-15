import os
from cloudinary_storage.storage import RawMediaCloudinaryStorage
import cloudinary.uploader


class LargeFileCloudinaryStorage(RawMediaCloudinaryStorage):
    """Custom storage for large files that uses Cloudinary's chunked upload"""
    
    def _upload(self, name, content):
        # Ensure file pointer is at the beginning
        if hasattr(content, 'seek'):
            try:
                content.seek(0)
            except (AttributeError, IOError, OSError):
                pass
        
        options = {'use_filename': True, 'resource_type': self._get_resource_type(name), 'tags': self.TAG}
        folder = os.path.dirname(name)
        if folder:
            options['folder'] = folder
        
        # Get actual file size correctly - be very careful here
        file_size = None
        
        # Try to get size from the file object
        if hasattr(content, 'size'):
            try:
                size_val = content.size
                if size_val is not None and isinstance(size_val, (int, float)) and size_val > 0:
                    file_size = int(size_val)
            except (AttributeError, TypeError):
                pass
        
        # If size attribute didn't work, try seek/tell method
        if file_size is None and hasattr(content, 'seek') and hasattr(content, 'tell'):
            try:
                # Save current position
                if hasattr(content, 'tell'):
                    try:
                        current_pos = content.tell()
                    except (IOError, OSError):
                        current_pos = 0
                else:
                    current_pos = 0
                
                # Seek to end to get file size
                content.seek(0, 2)
                file_size = content.tell()
                
                # Reset to beginning
                content.seek(current_pos)
            except (AttributeError, IOError, OSError):
                file_size = None
        
        # Ensure file pointer is at beginning
        if hasattr(content, 'seek'):
            content.seek(0)
        
        # Try to get file size - if we can reliably detect it's > 20MB, use chunked upload
        # Otherwise use regular upload (works up to plan limits, typically 10MB free tier)
        try:
            if hasattr(content, 'size') and content.size:
                file_size = content.size
                # Use chunked upload for files > 20MB (requires upgraded Cloudinary plan)
                if file_size > 20000000:
                    return cloudinary.uploader.upload_large(content, **options)
        except (AttributeError, TypeError):
            pass
        
        # Default to regular upload for smaller files or when size detection fails
        # Note: Free tier is limited to 10MB. For larger files, upgrade Cloudinary plan.
        return cloudinary.uploader.upload(content, **options)
