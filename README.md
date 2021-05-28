# Crawling_image
crawlig image to train the model

### I worked on ubuntu and when working with ubuntu, I had some problems while setting the google driver. So, I would like to share a solution to this part.
-------------------------------------------
1. Install chrome
2. Install chrome  driver
> $ google-chrome --version
> https://chromedriver.chromium.org/downloads
> $ unzip chromedriver_liux64.zip
3. Install selenium
> $ pip install selenium
4. Install beautifulsoup
> $ pip install beautifulsoup
5. Install others
> $ sudo pip istall xlrd
> $ sudo apt-get install xvfb
> $ sudo pip install pyvirtualdisplay
6. Setting driver
> $ sudo mv chromedriver /usr/bin/chromedriver
> $ sudo chown root:root  /usr/bin/chromedriver
> $ sudo chmod +x /ust/bin/chromedrier
> $ apt-get install -y unzip xvfb libxi6 libconf-2-4
> $ sudo apt-get install default-jdk
7. Change path
> Change the apth in the code to the absolute path where the chromedriver is located.

about selenium
https://selenium-python.readthedocs.io/getting-started.html
