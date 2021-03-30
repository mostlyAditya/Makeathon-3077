# Penny
This is our project for Makeathon 3077. This is a price comparison website that compares the prices fo various ecommerce website and shows you the best deal available for a particular product. 
<br/>
## Pre-requisite:
- `Python`  

## Steps to run project(VENV METHOD):  
- Run `install-dependencies.bat` to install the dependencies.
- Run `runsever.bat` to run the django testserver.
- Then open `localhost:8000` in the web browser.
<br/>

## Steps to run project(Docker Method):
- Make sure you have Docker installed on your system.
- In cmd, enter `docker push justshivam/penny:latest`.
- Then run the image by entering `docker run -p 8000:8000 justshivam/penny:latest` .
- open `localhost:8000` in web browser.
