from typing import Optional

from fastapi import FastAPI

app = FastAPI()



@app.put("/photos")
def add_photo(album_id):
    """Add a photo to an album.

    Store the photo on the server and transform the full quality photo into 
    """
    pass


@app.get("/photos/{id}")
def get_photo():
    """Download the photo at full resolution without the watermark.
    
    """
    pass


@app.get("/albums")
def list_albums():
    """List all the albums."""
    pass


@app.get("/albums/{album_id}")
def list_album_photos():
    """List all the photos in an album with their metadata."""
    pass



@app.get("/photos/preview/{id}")
def get_photo_preview():
    """Get a preview of a photo."""
    pass