from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import argparse


BROWSERS = [
    {'os': 'Windows', 'os_version': 'xp',
     'browser': 'IE', 'browser_version': '6.0'},
    {'os': 'Windows', 'os_version': 'xp',
     'browser': 'IE', 'browser_version': '7.0'},
    {'os': 'Windows', 'os_version': 'xp',
     'browser': 'firefox', 'browser_version': '3.6'},
    {'os': 'Windows', 'os_version': 'xp',
     'browser': 'firefox', 'browser_version': '29'},
    {'os' : 'OS X', 'browser' : 'safari',
     'os_version' : 'Snow Leopard', 'browser_version' : '5.1'},
    {'os' : 'Windows', 'browser_version' : '8.0',
     'os_version' : '7', 'browser' : 'ie'},
    {'os_version' : 'XP', 'browser_version' : '31.0',
     'browser' : 'chrome', 'os' : 'Windows'},
    ]

def format_browser(b):
    return '{browser}:{browser_version} on {os}:{os_version}'.format(**b) 

def format_short_browser(b):
    return '{browser}.{browser_version}.{os}.{os_version}'.format(**b) 

def get_file_name(b, click):
    base = 'shots/' + format_short_browser(b)
    if click:
        base += '.clicked'

    return base + '.png'


def get_shots(browsers):
    for cap in browsers:
        desired_cap = cap
        desired_cap['browserstack.local'] = True

        driver = webdriver.Remote(
            command_executor='http://OliverD1:81a6QnV3XQZsc95aBXwo@hub.browserstack.com:80/wd/hub',
            desired_capabilities=desired_cap)

        print '\n\n=================='
        print 'Fetching main shot for %s' % format_browser(cap)
        driver.get('http://localhost:8080')
        print 'Getting screen shot'
        driver.save_screenshot(get_file_name(cap, False))
        print 'Clicking on a menu item'
        driver.find_element_by_class_name('dropdown-button').click()
        print 'Getting screen shot'
        driver.save_screenshot(get_file_name(cap, True))

        driver.quit()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', '-l', action = 'store_true', default = False,
            help = 'List available browsers and exit.')
    parser.add_argument('--browser', '-b', action = 'append', default = None,
            help = 'Browser to test. Can be given multiple times')

    args = parser.parse_args()
    if args.list:
        for b in BROWSERS:
            print format_short_browser(b)
        return

    if args.browser is None:
        print 'Will grab screen shots for all browsers'
    else:
        valid_browser_names = {format_short_browser(x):x for x in BROWSERS}
        print 'Will grab screen shots for:'
        shots_to_get = []
        for b in args.browser:
            print b
            shots_to_get.append(valid_browser_names[b])
        get_shots(shots_to_get)

if __name__ == '__main__':
    main()
