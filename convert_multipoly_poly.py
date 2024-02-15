#%% Libraries
import geojson
from pathlib import Path

#%% Import input AOI file

input_file = input("Provie path to file:")
input_as_path = Path(input_file)

with open(f"{input_file}", 'r') as ir:
    data = geojson.load(ir)

input_file_name = input_as_path.stem
output_path = input_as_path.parent

print(input_file_name)

# %% Print length of file
print (len(data['features']))


# %% Build new FeatureCollection contaning the sigle polygons
out_geojson = geojson.FeatureCollection(features=[])

for feature in data['features']:
    if feature['geometry']['type'] == 'MultiPolygon':
        feature['geometry']['type'] = 'Polygon'
        feature['geometry']['coordinates'] =  feature['geometry']['coordinates'][0]  

        geometry = feature['geometry']
        properties = feature['properties']

        new_feature = geojson.Feature(geometry=geometry,
                                      properties=properties)

        print(new_feature)

        out_geojson['features'].append(new_feature)



# %% Write file
        
try:
    with open(f"./{output_path}/{input_file_name}_Poly.geojson", "w") as wd:
        geojson.dump(out_geojson, wd)

    print(f"File written")

except:
    print("error on write")
# %%
