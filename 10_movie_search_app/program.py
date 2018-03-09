import movie_svc
import requests.exceptions


def main():
    print_header()
    search_event_loop()


def print_header():
    print('---------------------------------')
    print('--------search movie app---------')
    print('---------------------------------')


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input("Movie search text (x to exit): ")
            if search != 'x':
                results = movie_svc.find_movies(search)
                print('Found {} results.'.format(len(results)))
                for r in results:
                    print('{} -- {}'.format(
                        r.year, r.title
                    ))
                print()
        except ValueError:
            print("Error: Search text is required")
        except requests.exceptions.ConnectionError as ce:
            print("Error: Your network is probably down")
        except Exception as x:
            print("Something goes wrong! Details: {}".format(x))

    print('exiting...')


if __name__ == '__main__':
    main()
