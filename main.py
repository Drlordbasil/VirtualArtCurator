import requests
from bs4 import BeautifulSoup


class Artwork:
    def __init__(self, title, artist, year, description, style, medium, image_url):
        self.title = title
        self.artist = artist
        self.year = year
        self.description = description
        self.style = style
        self.medium = medium
        self.image_url = image_url
        
    def display_info(self):
        print("Title:", self.title)
        print("Artist:", self.artist)
        print("Year:", self.year)
        print("Description:", self.description)
        print("Style:", self.style)
        print("Medium:", self.medium)
        
    def download_image(self, save_path):
        response = requests.get(self.image_url)
        with open(save_path, 'wb') as f:
            f.write(response.content)


class ArtGallery:
    def __init__(self):
        self.artworks = []
    
    def add_artwork(self, artwork):
        self.artworks.append(artwork)
    
    def collect_artworks(self, source_urls):
        for url in source_urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            artworks = soup.find_all('div', {'class': 'artwork'})
            for artwork in artworks:
                title = artwork.find('h2').text.strip()
                artist = artwork.find('p', {'class': 'artist'}).text.strip()
                year = artwork.find('p', {'class': 'year'}).text.strip()
                description = artwork.find('div', {'class': 'description'}).text.strip()
                style = artwork.find('p', {'class': 'style'}).text.strip()
                medium = artwork.find('p', {'class': 'medium'}).text.strip()
                image_url = artwork.find('img')['src']
                new_artwork = Artwork(title, artist, year, description, style, medium, image_url)
                self.add_artwork(new_artwork)
    
    def curate_virtual_exhibition(self, style, medium, historical_significance):
        curated_artworks = []
        for artwork in self.artworks:
            if artwork.style == style and artwork.medium == medium:
                curated_artworks.append(artwork)
        if curated_artworks:
            exhibition = VirtualExhibition(curated_artworks, historical_significance)
            return exhibition
        else:
            return None


class VirtualExhibition:
    def __init__(self, artworks, historical_significance):
        self.artworks = artworks
        self.historical_significance = historical_significance
        
    def display_exhibition(self):
        for artwork in self.artworks:
            artwork.display_info()


# Test the functionality of the program
if __name__ == '__main__':
    gallery = ArtGallery()
    
    # Collect artworks from online sources
    source_urls = ['https://www.example.com/source1', 'https://www.example.com/source2']
    gallery.collect_artworks(source_urls)
    
    # Curate a virtual exhibition
    style = 'Impressionism'
    medium = 'Oil on canvas'
    historical_significance = 4
    exhibition = gallery.curate_virtual_exhibition(style, medium, historical_significance)
    
    if exhibition:
        exhibition.display_exhibition()