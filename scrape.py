import os
import sys
import datetime as dt

import requests
import lxml.html


def main():

    ofname = 'jobnet.dat'
    url = 'https://job.jobnet.dk/CV'
    css_strs = [
        '#NoAvailablePositions strong',
        '#NoNewAvailablePositions strong',
        # This dissappeared sometime in august/september 2023 
        # '#NoActiveResumes strong',
        # This dissappeared i December 2024
        # '#NoPositionsDisplayedLastMonth strong',
    ]

    try:
        source_html = requests.get(url).text
    except Exception as e:
        print(e)
        raise SystemExit('Request failed ... Are you online?')

    tree = lxml.html.fromstring(source_html)

    stats = [
        tree.cssselect(css)[0].text.strip().replace('.', '').replace(',', '.')
        for css in css_strs]

    datestr = dt.datetime.now().isoformat()[:16]

    output_line = '{}\n'.format(';'.join([datestr] + stats))
    with open(ofname, 'a', encoding='utf-8') as fsock:
        fsock.write(output_line)


if __name__ == '__main__':
    main()
