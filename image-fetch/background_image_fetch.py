import urllib.request
import cv2


def get_urls():
    with open('./image-link.txt', 'r') as data:
        return data.readlines()


def download_images(urls):
    for index, url in enumerate(urls):
        print(url)
        path = './images/' + str(index) + '.jpg'
        urllib.request.urlretrieve(url, path)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        resized_img = cv2.resize(img, (100, 100))
        cv2.imwrite(path, resized_img)
        

urls = get_urls()
download_images(urls)
