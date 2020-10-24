from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.get('http://ovh.net')
import time
######### XPATHS ############################
## Start Button - /html/body/div/div/div[2]/div[12]/div/button[1]
## Select Server button - /html/body/div/div/div[2]/div[6]/button
## Servers - /html/body/div/div/div[2]/div[13]/div[5]/div[4]
## html body div.Main div div.SpeedTest div.serverPanel.welcomeState button.selectServerButton
## Server Button - /html/body/div/div/div[2]/div[13]/div[5]/div[1]/button
## Till 36
## Restart Button - /html/body/div/div/div[2]/div[12]/div/button[2]

## div.pool:nth-child(1) > button:nth-child(1)
## div.pool:nth-child(2) > button:nth-child(1)

################# Download ##################
## Average Value - /html/body/div/div/div[2]/div[5]/div[5]
## Peak Value - /html/body/div/div/div[2]/div[5]/div[7] 

############# Upload ########################
## Average - /html/body/div/div/div[2]/div[5]/div[15]
## Peak - /html/body/div/div/div[2]/div[5]/div[17]

############Latency######################
## Minimum - /html/body/div/div/div[2]/div[5]/div[29]
## Average - /html/body/div/div/div[2]/div[5]/div[25]
## Jitter - /html/body/div/div/div[2]/div[5]/div[27]

f = open("demofile.csv", "a")
f.write("Avg Download,Peak Download,Avg Upload,Peak Upload,Minimum Latency,Average Latency, Jitter")
f.write("\n")

def write_file():
	f = open("demofile.csv", "a")
	for i in result_list:
		f.write(i+',')
	f.write("\n")
	f.close()



time.sleep(60)

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  # Changing to iframe of nperf plugin

time.sleep(5)

elem = driver.find_element_by_css_selector('button.selectServerButton:nth-child(1)') # To click on Server Select Button
elem.click()

time.sleep(5)

elem = driver.find_element_by_css_selector('div.pool:nth-child(1) > button:nth-child(1)') # To select the First server in the list
elem.click()

time.sleep(5)

elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[12]/div/button[1]") # To click on Start 
elem.click()

time.sleep(90)

result_list=[]

elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[5]") # To select the avg down speed block
val1=elem.text # fetching the avg down speed

result_list.append(val1)

elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[7]") # To select the peak down speed block
val1=elem.text # fetching the peak down speed

result_list.append(val1)

elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[15]") # To select the avg up speed block
val1=elem.text # fetching the avg up speed

result_list.append(val1)

elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[17]") # To select the peak up speed block
val1=elem.text # fetching the peak up speed

result_list.append(val1)

elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[29]") # To select the min
val1=elem.text # fetching the min

result_list.append(val1)

elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[25]") # To select the avg lat
val1=elem.text # fetching the avg lat

result_list.append(val1)

elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[27]") # To select the jitter
val1=elem.text # fetching the jitter

result_list.append(val1)


print(result_list)

## /html/body/div/div/div[2]/div[5]/div[5]

# server_list=[]
# a=1
# for i in range(2,37):
# 	i=str(i)
# 	server_list.append("/html/body/div/div/div[2]/div[13]/div[5]/div["+i+"]/button")

#print(server_list[0])
f = open("demofile.csv", "a")
for i in result_list:
	f.write(i+',')
f.write("\n")
f.close()

for i in range(2,37):
	result_list=[]
	i=str(i)

	time.sleep(5)

	elem = driver.find_element_by_css_selector('button.selectServerButton:nth-child(1)') # To click on Server Select Button
	elem.click()

	time.sleep(7)

	elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[13]/div[5]/div["+i+"]/button") # To select the second server in the list
	elem.click()

	time.sleep(5)


	elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[12]/div/button[2]") # To click on Restart
	elem.click()

	time.sleep(90)

	elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[5]") # To select the avg down speed block
	val1=elem.text # fetching the avg down speed

	result_list.append(val1)

	elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[7]") # To select the peak down speed block
	val1=elem.text # fetching the peak down speed

	result_list.append(val1)

	elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[15]") # To select the avg up speed block
	val1=elem.text # fetching the avg down speed

	result_list.append(val1)

	elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[17]") # To select the peak up speed block
	val1=elem.text # fetching the peak up speed

	result_list.append(val1)

	elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[29]") # To select the min
	val1=elem.text # fetching the min

	result_list.append(val1)

	elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[25]") # To select the avg lat
	val1=elem.text # fetching the avg lat

	result_list.append(val1)

	elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/div[27]") # To select the jitter
	val1=elem.text # fetching the jitter

	result_list.append(val1)

	print(result_list)

	write_file()