import geopandas as gpd
import networkx as nx
import pandas as pd


class BusRoutes():
    def __init__(self):
        self._stop_names = {}  # id: name
        self._route_names = {}  # id: name

        self._route_nodes = []  # stop_id
        self._route_edges = []  # start_stop_id-end_stop_id: dist
        self._route_stop_count = {}  # stop_id: count
        self._route_stop_time_count = {}  # stop_id-half hour-day: count
        self._gx = nx.DiGraph()

        self._load_schedule()
        self._load_routes()

    def _load_schedule(self, 
                       stops_path: str = 'data/GTFS/stop_times.txt',
                       trip_path: str = 'data/GTFS/trips.txt',
                       route_path: str = 'data/GTFS/routes.txt'):
        """Load the PRT schedule, from GTFS data at 
        https://www.rideprt.org/business-center/developer-resources/"""
        df = pd.read_csv(stops_path, dtype={'stop_id': 'str'}).merge(
                pd.read_csv(trip_path)[['trip_id', 'route_id', 'direction_id']], how='left', on='trip_id').merge(
                pd.read_csv(route_path, dtype={'route_short_name': 'str'})[['route_id', 'route_short_name', 'route_long_name']], how='left', on='route_id'
            )
        self._route_nodes = df['stop_id'].unique().tolist()
        for sid, sname in df[['stop_id', 'stop_headsign']].unique():
            self._stop_names.set(sid, sname)
        for rid, rname in df[['route_id', 'route_long_name']].unique():
            self._route_names.set(rid, rname)

        df.groupby(['route_id', 'direction_id', 'trip_id']).apply(
            lambda route: self._load_route_schedule(route), axis=1)

    def _load_route_schedule(self, df: pd.DataFrame):
        """Extract a route schedue in load_schedule."""
        df = df.sort_values(['stop_sequence'])
        for row in df.itertuples():
            key = row['stop_id']
            self._route_stop_count.set(key, self._route_stop_count.get(key, 0) + 1)
            
            row['stop_id']

        for row1, row2 in zip(df[:-1].itertuples(index=False), df[1:].itertuples(index=False)):


    def _load_routes(self, path: str = 'data/prt_routes.geojson'):
        """Load the PRT routes to compute stop distances at
        https://data.wprdc.org/dataset/prt-current-transit-routes"""
        routes = gpd.read_file('data/prt_routes.geojson')
        print(routes)


if __name__ == '__main__':
    br = BusRoutes()