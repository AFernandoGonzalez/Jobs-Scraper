import requests
import csv
from bs4 import BeautifulSoup

# exporting to csv
outfile = open('Job Listing.csv', 'w', newline='')
writer = csv.writer(outfile)
writer.writerow(["Job Title", "Job Location", "Job Date", "Job Position", "Company", "Job Description"])

# get the url website
url = requests.get('https://pythonjobs.github.io/')

# getting the status code of the website
page = (url)

# crrating a beautiful soup object
soup = BeautifulSoup(page.content, 'html.parser')


# results of the page
results = soup.find(id='content')

# finding blog posts
blog_elements = results.find_all('div', class_='job')

# loop through each div post
for blog_element in blog_elements:

    job_title = blog_element.find_all('a')[1]
    job_location = blog_element.find_all('span')[0]
    job_date = blog_element.find_all('span')[1]
    job_position = blog_element.find_all('span')[2]
    company = blog_element.find_all('span')[3]
    job_description = blog_element.find('p', class_='detail')
    

    # getting the text only
    j_title = job_title.text.strip()
    j_location = job_location.text.strip()
    j_date = job_date.text.strip()
    j_position = job_position.text.strip()
    j_company = company.text.strip()
    j_description = job_description.text.strip()

    # writing it on the csv file
    writer.writerow([j_title, j_location, j_date, j_position, j_company, j_description])

    # print('Job Title: ' + j_title)
    # print('Job Location: ' + j_location)
    # print('Job Date: ' + j_date)
    # print('Job Company: ' + j_company)
    # print('Job Description: ' + j_description)
    # print(end='\n'*3)

outfile.close()
