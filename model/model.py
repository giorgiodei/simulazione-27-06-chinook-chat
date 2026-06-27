import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists = []
        self._idMapArtists = {}

    def getAllGenre(self):
        return DAO.getAllGenre()

    def getAllCountries(self):
        return DAO.getAllCountries()

    def creaGrafo(self, genre, country, valore):
        self._graph.clear()

        self._artists = DAO.getAllNodes(genre, country, valore)
        self._idMapArtists = {a.ArtistId: a for a in self._artists}
        self._graph.add_nodes_from(self._artists)

        coppiewpeso = DAO.getEdgeswPeso(genre, country)
        for row in coppiewpeso:
            idA, idB, peso = row["idA"], row["idB"], row["peso"]
            if idA in self._idMapArtists and idB in self._idMapArtists:
                artistaA = self._idMapArtists[idA]
                artistaB = self._idMapArtists[idB]
                self._graph.add_edge(artistaA, artistaB, weight=peso)


    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getInfoComponenti(self):
        componenti = list(nx.connected_components(self._graph))
        componente_maggiore = max(componenti, key=len) if componenti else set()
        return len(componenti), componente_maggiore

    def getTopKArchi(self, k=5, massimo=True):
        archi = []
        for u, v, data in self._graph.edges(data=True):
            peso = data.get("weight", 0)
            archi.append((u, v, peso))
        archi.sort(key=lambda x: x[2], reverse=massimo)
        return archi[:k]