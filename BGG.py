from bs4 import BeautifulSoup
import requests
import re
import json


def get(browse_link):
    browse_dict = {
        'Name': [],
        'BGG_Rating': [],
        'AVG_Rating': [],
        'Voter_Count': [],
        "Min_Players": [],
        "Max_Players": [],
        "Min_Time": [],
        "Max_Time": [],
        "Min_Age": [],
        "Difficulty": [],
        "Owners": [],
        "Total_Plays": [],
    }

    soup = BeautifulSoup(
        requests.get(browse_link).text,
        'html5lib')

    all_links = soup.find_all('a', attrs={'href': re.compile("^/boardgame/.")})
    main100_links = all_links[1::3]

    all_stats = soup.find_all('td', attrs={'class': 'collection_bggrating'})

    for idx in range(100):
        adjusted_idx = idx * 3
        current_link = main100_links[idx].get('href')

        browse_dict['Name'].append(main100_links[idx].text)
        browse_dict['BGG_Rating'].append(get_num(all_stats[adjusted_idx].text))
        browse_dict['AVG_Rating'].append(get_num(all_stats[adjusted_idx + 1].text))
        browse_dict['Voter_Count'].append(get_num(all_stats[adjusted_idx + 2].text))

        stats = get_stats(current_link)
        browse_dict['Min_Players'].append(stats['minplayers'])
        browse_dict['Max_Players'].append(stats['maxplayers'])
        browse_dict['Min_Time'].append(stats['minplaytime'])
        browse_dict['Max_Time'].append(stats['maxplaytime'])
        browse_dict['Min_Age'].append(stats['minage'])
        browse_dict['Difficulty'].append(stats['avgweight'])
        browse_dict['Owners'].append(stats['numowned'])
        browse_dict['Total_Plays'].append(stats['numplays'])

    return browse_dict


def get_num(string):
    return float(re.search('\S+', string).group(0))


def get_stats(link_ext):
    html_str = (requests
                .get(f'https://boardgamegeek.com{link_ext}/stats')
                .text)

    info_str = ('{' + html_str[
                      html_str.find('"minplayers":'):
                      html_str.find(',', html_str.find('"minage":'))]
                + '}')
    game_info = json.loads(info_str)

    for key in game_info:
        game_info[key] = int(game_info[key])

    stats_idx = html_str.find('"stats"')
    stats_str = html_str[
                stats_idx + 8:
                stats_idx + html_str[stats_idx:].find('}') + 1]
    messy_game_stats = json.loads(stats_str)

    important_stats_keys = ['avgweight', 'numowned', 'numplays']
    game_stats = {key: messy_game_stats[key] for key in important_stats_keys}

    for key in game_stats:
        game_stats[key] = float(game_stats[key])

    return {**game_info, **game_stats}
