from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import argparse
import sys

def format_browser(b):
    return '{browser}.{browser_version}.{os}.{os_version}'.format(**b) 

def get_file_name(b, click):
    base = 'shots/' + format_browser(b)
    if click:
        base += '.clicked'

    return base + '.png'


def get_shots(browsers):
    for cap in browsers:
        try:
            desired_cap = cap
            desired_cap['browserstack.local'] = True

            driver = webdriver.Remote(
                command_executor = 'http://OliverD1:81a6QnV3XQZsc95aBXwo@hub.browserstack.com:80/wd/hub',
                desired_capabilities = desired_cap)

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
        except Exception as e:
            print 'Error getting shots for ', format_browser(cap)
            f = open('shots/%s.errors' % format_browser(cap), 'w+')
            f.write(str(e))
            f.close()

def get_browser_list():
    # Load the list of available browsers from a file. This file was obtained by
    # running:
    #
    # curl -u "OliverD1:81a6QnV3XQZsc95aBXwo" \
    #       https://www.browserstack.com/automate/browsers.json
    browser_file = open('browser-list.txt')
    browsers = json.load(browser_file)
    for b in browsers:
        if b['device'] is None:
            del(b['device'])
    return browsers

def main():
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
    parser.add_argument('--list', '-l', action = 'store_true', default = False,
            help = 'List available browsers and exit.')
    parser.add_argument('--browser', '-b', action = 'append', default = None,
            help = 'Browser to test. Can be given multiple times')

    BROWSERS = get_browser_list()

    args = parser.parse_args()
    if args.list:
        for b in BROWSERS:
            print format_browser(b)
        return

    if args.browser is None:
        print 'Error: you must supply at least one browser'
        parser.print_help()
        sys.exit(1)
    else:
        valid_browser_names = {format_browser(x):x for x in BROWSERS}
        print 'Will grab screen shots for:'
        shots_to_get = []
        for b in args.browser:
            print b
            shots_to_get.append(valid_browser_names[b])
        get_shots(shots_to_get)

if __name__ == '__main__':
    main()
