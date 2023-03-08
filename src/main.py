from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import smtplib
from bs4 import BeautifulSoup
from email.message import EmailMessage

import config

CHROMEDRIVER_PATH = './src/chromedriver.exe'

def main():
    
    # driver = setupWebDriver()
    
    # emails_to_be_opened = retriveAllEmailsOnSinglePage(driver)

    # collection_subjects_and_messages = openEmailsAndExtractText(driver, emails_to_be_opened)

    # for i in collection_subjects_and_messages:
    #     for j in i:
    #         print(j)
    #     print('\n\n---------------------------------------------------\n\n')

    collection_subjects_and_messages = test_scraped_subject_and_message()

    sendEmail(collection_subjects_and_messages)

    # driver.close()
    # driver.quit()

def sendEmail(collection_subjects_and_messages):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login(config.g_username, config.g_password)

    for i in collection_subjects_and_messages:
        subject = i[0]
        message = i[1]

        msg = EmailMessage()
        msg.set_content(message)

        msg['Subject'] = 'Letter From Griffin - ' + subject
        msg['From'] = config.g_username
        msg['To'] = config.g_username
    
        # sending the mail
        s.send_message(msg)

        # 5 second delay to slow things down
        time.sleep(5)
    
    # terminating the session
    s.quit()

    
def openEmailsAndExtractText(driver, emails_to_be_opened):

    wait = WebDriverWait(driver, 10)
    collection_subjects_and_messages = []

    for e in emails_to_be_opened:
        single_subject_and_message = []
        single_subject_and_message.append(e.text.strip())

        wait.until(EC.presence_of_element_located((By.LINK_TEXT, e.text.strip())))
        message_link = driver.find_element(by=By.LINK_TEXT, value=e.text.strip())
        message_link.click()
        wait.until(EC.presence_of_element_located((By.ID, 'messageForm')))
        html = driver.page_source
        soup = BeautifulSoup(html, 'html5lib')
        form = soup.find('form', id='messageForm')
        fieldset = form.find('fieldset')
        divs = fieldset.find_all('div')
        paragraphs = divs[5].find_all('p')
        message_text = ''
        for p in paragraphs:
            if len(p.text) == 0:
                continue
            message_text += p.text + '\n\n'
        single_subject_and_message.append(message_text)
        collection_subjects_and_messages.append(single_subject_and_message)

        driver.execute_script("window.history.go(-1)")

    return collection_subjects_and_messages    

def retriveAllEmailsOnSinglePage(driver):
    wait = WebDriverWait(driver, 10)

    driver.get(config.webpage_url)
    wait.until(EC.element_to_be_clickable((By.ID, 'cnForm:returnToLogin'))).click()

    wait.until(EC.element_to_be_clickable((By.ID, 'user_email'))).send_keys(config.connect_username)
    wait.until(EC.element_to_be_clickable((By.ID, 'user_password'))).send_keys(config.connect_password)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Messaging"))).click()

    # Wait to give time for page to completely load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'wrapper')))

    html = driver.page_source
    soup = BeautifulSoup(html, 'html5lib')
    table = soup.find('tbody', id=lambda L: L and L.startswith('messagesForm'))
    rows = table.find_all('tr')
    emails_to_be_opened = []
    for r in rows:
        row_table_data = r.find_all('td')
        message_link = row_table_data[1].find('a')
        classes = message_link.attrs['class']
        if 'bold' not in classes:   # to be changed to "if 'bold' in classes" when testing is finished. 
            emails_to_be_opened.append(message_link)
    return emails_to_be_opened

def setupWebDriver():
    options = Options()
    # Keeps the browser open
    options.add_experimental_option("detach", True)
    # Browser is displayed in a custom window size
    options.add_argument("window-size=1500,1000")
    # Removes the "This is being controlled by automation" alert / notification
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # to supress the error messages/logs
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(CHROMEDRIVER_PATH)
    return Chrome(service=service, options=options)

def test_scraped_subject_and_message():
    collection_subjects_and_messages = []
    first_subject_and_message = []
    second_subject_and_message = []

    message1 = '''Genesis 2:2 "And on the seventh day God finished his work that he had done, and he rested on the seventh day from all his work that he had done."

There was work before the fall; there will be work after the fall; for work is of God... Christians may not fully understand this doctrine. Believe it or not, in the old world, places like Rome despised the idea of work- they felt it was beneath their dignity. For this reason Empires' like Rome forced slaves to do all the manual labor: even professions like lawyers, doctors, cooks, and cleaners. A Roman citizen made everyone else do the work while they watched the games.

When Christians came on the scene they caused a paradigm shift in this area, for their God worked, and they were taught to do all things to the "glory of the Lord". The Jesus followers elevated the idea of work and made it something honorable to the masses.

Christians haved worked more than any other group in bringing about good changes to the worldview, for example:

•Christians started most hospitals, hospices, and medical clinics.

•Nearly all of the first 123 American universities were started by Christians to teach others how to learn from the Bible!

•Before the Civil war 2\3 of abolition societies were headed by pastors.

•Before Christianity, cannibalism was widespread, and Anglo-Saxons drank human blood- it was the Gospel that civilized barbaric cultures.

•Modern science- The vast majority of scientific discoveries are from Christian-based countries.

•Capitalism and free-enterprise- Christianity is directly responsible for work discipline, self-reliance, and self-denial.

•Elevation of women- No other religion elevates women to equality with men.

And this is just a short list of the fruits of the Christian Spirit. Before you let 'Woke' culture poison your mind, happily remind them of some of these very things. You are the light of the World!

In Christian Love'''

    message2 = '''Luke 23:46 "Then Jesus, calling out with a loud voice, said, 'Father, into your hands I commit my spirit!' And having said this he breathed his last."

The word commit in this verse is the Greek Paratithemi (par-at-ith'-ay-mee), it means: to place alongside, i.e. present (food, truth); by impl. to deposit (as a trust or for protection).

From this beautiful verse we learn that Jesus, the Son of God, totally trusted the Father with his life. From the manger to the tomb, the walk of Jesus was continual trust in the Almighty; no one has ever been more sure of God's goodness! Even in the darkest of times, Christ walked, as seeing Him who is invisible.

To have this heartfelt trust should be the goal of every Christian.

Jesus knew that God the Father would vindicate him. His whole life was one of complete surrender to the will of God. Sometimes it is hard to discern the purpose of God; but this should not make our faith waver. If we do what is right according to the will of God then He will make our cause come out to be right in the end. We must commit our spirit and life to the hands' that hold all things. We deposit our future and existence into God's trust- who is the Fort Knox of human souls.

When we give our life over to God He will give it back to us- at the Resurrection. We entrust, our spirit, into the hands of God, and He will hold it for safe-keeping. Invest your life in God and eternity will be the return. Invest your life in the world and you will not receive much. All who hope for the future must follow the steps of Jesus. We present our future unto God's decision and reliance. We have confidence that the Almighty will place us into His security deposit box; stored like a precious treasure; safe from all thievery and robbers. Amen.

In Christian Love'''


    first_subject_and_message.append('Work Is From God')
    first_subject_and_message.append(message1)

    second_subject_and_message.append('I Commit My Spirit')
    second_subject_and_message.append(message2)

    collection_subjects_and_messages.append(first_subject_and_message)
    collection_subjects_and_messages.append(second_subject_and_message)


    return collection_subjects_and_messages

if __name__ == "__main__":
    main()
