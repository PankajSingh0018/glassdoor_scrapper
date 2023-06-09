# Running the loop over the main element page that stores all the information to get the required detail and append the value to the list

for element in elements[:2]:
    element.click()
    sleep(5)

    # Finding the title for the job posted 
    title= driver.find_element(By.CLASS_NAME,"job-title.mt-xsm").text
    print(title)
    sleep(2)

#     # Organisation name 
#     org_name = driver.find_element(By.CLASS_NAME,'ml-xsm.job-search-1bgdn7m').text
#     Org = org_name
#     # print(f'Organisation Name',Org)
#     sleep(2)

#     # Finding the Job link from the web-content
#     link= driver.find_element(By.CLASS_NAME,'p-std.jobCard')
#     job_link= link.get_attribute('href')
#     # print(job_link)
#     sleep(2)

    
#     #location 
#     location = driver.find_element(By.CLASS_NAME,'location.mt-xxsm').text
#     # print(f"Location :",location)
#     sleep(2)

#     #Salary Range
#     try:
#         salary = driver.find_element(By.CLASS_NAME,'salary-estimate').text
#         sal= salary.split()[2]
#         # print(f'Salary:',sal)
#     except:
#         " "
#     sleep(2)
#     j_d= driver.find_element(By.CLASS_NAME,'jobDescriptionContent.desc').text
#     #print(j_d)
#     sleep(2)
        
#     details.append({
#                 'Job Title': title,
#                 'Organisation Name' : Org, 
#                 'Job Link' : job_link,
#                 'Location' : location,
#                 'Salary' : sal
#                 # 'Job Description' : j_d

#     })

# df =pd.DataFrame.from_dict(details)
# df.to_csv("Glassdoor_Jobs",index=None)
# # df.to_excel("Glassdoor_jobs.xlsx",index=None)