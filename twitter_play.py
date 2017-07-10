from TwitterSearch import *

try:
    tso = TwitterSearchOrder()
    tso.set_keywords(['Guttenberg', 'Doktorarbeit'])
    tso.set_language('de')
    tso.set_include_entities(False)

    ts = TwitterSearch(
        consumer_key= 'XWO5mY7F48hhdQJzL3STgaOqM',
        consumer_secret= 'DjMO3pKlsMpog423baSaM7AfCCVMuXHbIeALbh9ZHUi38UJsLw',
        access_token = '883524855777288192-FKbTuepIKEo8GrrcJkzPaVL7SxhCMoN',
        access_token_secret='jWNhJd5LcTnmMon6X7C1dRsJUQeKLLsiV17MYcRCpHJTE')

    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)



