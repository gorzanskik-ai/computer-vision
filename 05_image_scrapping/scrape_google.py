from google_images_download import google_images_download

# https://chromedriver.chromium.org/downloads

response = google_images_download.googleimagesdownload()

search_querries = ['horse', 'lion']


def download_images(query):
    arguments = {
        'keywords': query,
        'format': 'jpg',
        'limit': 50,
        'print_urls': True,
        'size': 'medium',
        #'aspect_ratio': 'square',
        #'chromedriver': r'C:\Users\gorza\chrome-driver\chromedriver.exe'
    }

    try:
        response.download(arguments)
    except FileNotFoundError:
        arguments = {
            'keywords': query,
            'format': 'jpg',
            'limit': 50,
            'print_urls': True,
            'size': 'medium',
            #'chromedriver': r'C:\Users\gorza\chrome-driver\chromedriver.exe'
        }
        try:
            response.download(arguments)
        except:
            pass


for query in search_querries:
    download_images(query)
    print()
