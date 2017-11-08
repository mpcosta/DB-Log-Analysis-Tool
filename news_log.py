#!/usr/bin/python3

import psycopg2

DBNAME = "news"

def get_most_popular_artc(x):
    """Prints out the X most popular articles of the news database"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT title, views FROM articles \
               LEFT JOIN (SELECT path, count(*) AS views FROM log GROUP BY path) AS popular_articles \
               ON path LIKE '%%' || slug \
               ORDER BY views DESC \
               LIMIT %s", (x,))
    query_results = c.fetchall()
    # Check Query List Size and Compare with size Requested in x param
    if len(query_results) < int(x):
        print("\nUnfortunately this database does not contain %s Articles." % (x,))
        x = len(query_results);
        print("\nInstead we will be showing you all the %s Articles available.\n" % (x,))
    # Print out the X most popular articles
    print("\nThe %s Most Popular Articles of all time are:\n" % (x,))
    for title, views in query_results:
        print("%s - %d Views" % (title, views))
    print("\n")
    db.close()


def get_most_popular_authors():
    """Prints out the most popular authors of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT name, sum(views) FROM authors, articles \
               LEFT JOIN (SELECT path, count(*) AS views FROM log GROUP BY path) AS all_articles \
               ON path LIKE '%%' || slug \
               WHERE authors.id = articles.author GROUP BY authors.id")
    query_results = c.fetchall()
    print("\nThe Most Popular Authors of all time are:\n")
    for author, views in query_results:
        print("%s - %d Views" % (author, views))
    print("\n")
    db.close()


def get_most_err_req(x):
    """Prints out the days in which more than X %% of requests led to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT notOKStatus.dates, (notOKStatus.total*100.0/allStatus.total) AS percentColumn \
               FROM (SELECT CAST(time AS DATE) AS dates, count(status) AS total FROM log \
               WHERE status NOT LIKE 200 || '%%' GROUP BY dates) AS notOKStatus \
               JOIN (SELECT CAST(time AS DATE) AS dates, count(status) AS total FROM log \
               GROUP BY dates) AS allStatus \
               ON notOKStatus.dates = allStatus.dates WHERE (notOKStatus.total*100.0/allStatus.total) > %s", (x,))
    query_results = c.fetchall()
    # Check Query List Size and Compare with percentage Requested in x param
    if len(query_results) <= 0:
        print("\nUnfortunately we could not find any results that led to more than %s Percent." % (x,))
        print("Pleasy try again with a different percentage value. \n")
    else:
        # Print out the days that more than X percent of requests lead to errors
        print("\nThe Dates in which more than %s %% of requests led to errors are:\n" % (x,))
        for author, views in query_results:
            print("%s - %.2f %%" % (author, views))
        print("\n")
    db.close()


def main():
    get_most_popular_artc(3);
    get_most_popular_authors();
    get_most_err_req(1);


if __name__ == '__main__':
    main();
