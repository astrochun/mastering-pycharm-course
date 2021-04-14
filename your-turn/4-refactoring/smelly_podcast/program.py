from service import Episode, episode_data, get_latest_show_id, download_data, get_episode


def main():
    # SHOW THE HEADER
    show_header()

    # DOWNLOAD THE EPISODE DATA
    download_data()

    # GET LATEST SHOW ID
    latest_show_id = get_latest_show_id()
    oldest_show_id = min(episode_data.keys())

    print("Working with total of {} episodes".format(latest_show_id))

    # DISPLAY RESULTS
    display_results(latest_show_id, oldest_show_id)


def display_results(latest_show_id, oldest_show_id):
    start = oldest_show_id
    end = latest_show_id + 1
    for show_id in range(start, end):
        # GET EPISODE
        info = get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


def show_header():
    print("Welcome to the talk python info downloader.")
    print()


if __name__ == '__main__':
    main()
