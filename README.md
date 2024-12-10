# CS210 Final Project -> Follow Order of Folders as...

If you have any questions please reach out 

Project Report: in the CS210 Project Report.pdf file

1. webScraping:
   MUST INSTALL PLAYWRIGHT FOR THIS TO WORK ON YOU OWN COMPUTER!!!

   run: pip install playwright

   in the terminal

   Scraped the web for NBA Data about team offenses in the 2023-24 season. I gathered statistics on teams Offensive Ratings, the type of shots teams took, and player offensive statistics. data that was scraped was formatted and saved into CSVs

3. CSVs:

   Stored the values that are going into the database into a CSV first, due to the information that was scraped being on multiple pages and not being able to insert it into a DB while scraping.

4. CREATEDATABASE:

   Used sqlite3 to create NBAOFFENSE database and NBATEAMS/NBAPLAYERS tables by pulling data from the csvs in the CSVs folder. There are also extra files I used to test out the DB

5. QueriesAndML:

   Implemented a k-means clustering algorithm in the Kmeans.py file used it in the QueryAndKmeans.py folder on specific queries from the database.

6. GRAPHS:

   Visualized the kmeans algorithm, along with the relationship between loss and number of clusters to determine the optimal number of centroids.

7. NBAOFFENSE.db: this contains the database created in the CREATEDATABASE folder. Contains tables NBAPLAYERS and NBATEAMS
