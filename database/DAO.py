# DAO.py

from database.DB_connect import DBConnect
from model.artist import Artist


class DAO:

    @staticmethod
    def getAllGenre():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """select g.Name as name
                   from genre g"""
        cursor.execute(query)

        for row in cursor:
            result.append(row["name"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """select distinct c.Country as paese
from customer c """
        cursor.execute(query)

        for row in cursor:
            result.append(row["paese"])

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllNodes(genere, paese,valore):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
            select distinct ar.*
from artist ar, album al, track t, genre g,
invoiceline riga, invoice fatt, customer c 
where ar.ArtistId =al.ArtistId  and t.AlbumId =al.AlbumId
and t.GenreId =g.GenreId and g.Name =%s  and riga.TrackId =t.TrackId 
and riga.InvoiceId =fatt.InvoiceId and c.CustomerId =fatt.CustomerId 
and c.Country =%s 
group by ar.ArtistId 
having SUM(riga.UnitPrice * riga.Quantity)>=%s 
    """
        cursor.execute(query, (genere, paese,valore,))

        for row in cursor:
            result.append(Artist(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdgeswPeso(genere, paese):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
            select ar1.ArtistId as idA, ar2.ArtistId as idB, count(distinct c1.CustomerId) as peso
from artist ar1, album al1, track t1, genre g1,
     invoiceline riga1, invoice fatt1, customer c1,
     artist ar2, album al2, track t2, genre g2,
     invoiceline riga2, invoice fatt2, customer c2
where c1.CustomerId = c2.CustomerId
  and ar1.ArtistId < ar2.ArtistId
  and ar1.ArtistId = al1.ArtistId
  and t1.AlbumId = al1.AlbumId
  and riga1.TrackId = t1.TrackId
  and riga1.InvoiceId = fatt1.InvoiceId
  and c1.CustomerId = fatt1.CustomerId
  and t1.GenreId = g1.GenreId
  and g1.Name = %s
  and ar2.ArtistId = al2.ArtistId
  and t2.AlbumId = al2.AlbumId
  and riga2.TrackId = t2.TrackId
  and riga2.InvoiceId = fatt2.InvoiceId
  and c2.CustomerId = fatt2.CustomerId
  and t2.GenreId = g2.GenreId
  and g2.Name = %s
  and c1.Country = %s
group by ar1.ArtistId, ar2.ArtistId
        """
        cursor.execute(query, (genere, genere,paese))
        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result


