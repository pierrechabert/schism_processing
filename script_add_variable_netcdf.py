import xarray as xr
import numpy as np

def add_variables(filename_i, filename_o):

    ds = xr.open_dataset(filename_i)

    ds['time'].attrs['standard_name'] = 'time'
    ds['time'].attrs['axis'] = 'T'

    ds['minimum_depth'].attrs['units'] = 'm'

    ds['depth'].attrs['units'] = 'm'
    ds['depth'].attrs['axis'] = 'Z'
    ds['depth'].attrs['positive'] = 'down'
    ds['depth'].attrs['coordinates']= 'SCHISM_hgrid_node_x SCHISM_hgrid_node_y'
    ds['depth'].attrs['location'] = 'node'
    ds['depth'].attrs['grid_mapping'] = 'crs'
    ds['depth'].attrs['mesh'] = 'SCHISM_hgrid'

    ds['bottom_index_node'].attrs['coordinates'] = 'SCHISM_hgrid_node_x SCHISM_hgrid_node_y'
    ds['bottom_index_node'].attrs['location'] = 'node'
    ds['bottom_index_node'].attrs['grid_mapping'] = 'crs'
    ds['bottom_index_node'].attrs['mesh'] = 'SCHISM_hgrid'

    ds['elevation'].attrs['coordinates'] = "SCHISM_hgrid_node_x SCHISM_hgrid_node_y"
    ds['elevation'].attrs['grid_mapping'] = "crs"
    ds['elevation'].attrs['location'] = "node"

    ds['SCHISM_hgrid_node_x'].attrs['axis'] = "X"
    ds['SCHISM_hgrid_node_x'].attrs['location'] = "node"
    ds['SCHISM_hgrid_node_x'].attrs['mesh'] = "SCHISM_hgrid" 
    ds['SCHISM_hgrid_node_x'].attrs['units'] = "degree_E"
    ds['SCHISM_hgrid_node_x'].attrs['standard_name'] = "longitude"

    ds['SCHISM_hgrid_node_y'].attrs['axis'] = "Y"
    ds['SCHISM_hgrid_node_y'].attrs['location'] = "node"
    ds['SCHISM_hgrid_node_y'].attrs['mesh'] = "SCHISM_hgrid"
    ds['SCHISM_hgrid_node_y'].attrs['units'] = "degree_N"
    ds['SCHISM_hgrid_node_y'].attrs['standard_name'] = "latitude"

    ds['SCHISM_hgrid_face_nodes'].attrs['start_index'] = 1
    ds['SCHISM_hgrid_face_nodes'].attrs['_FillValue'] = -1
    ds['SCHISM_hgrid_face_nodes'].attrs['cf_role'] = "edge_node_connectivity"

    ds['SCHISM_hgrid_edge_nodes'].attrs['start_index'] = 1
    ds['SCHISM_hgrid_edge_nodes'].attrs['_FillValue'] = -1
    ds['SCHISM_hgrid_edge_nodes'].attrs['cf_role'] = "edge_node_connectivity"

    ds['dryFlagNode'].attrs['location'] = "node"
    ds['dryFlagNode'].attrs['coordinates'] = "SCHISM_hgrid_node_x SCHISM_hgrid_node_y" 
    ds['dryFlagNode'].attrs['grid_mapping'] = "crs"
    ds['dryFlagNode'].attrs['mesh'] = "SCHISM_hgrid"

    idmask = ds['idmask'].values  # (node,)
    elev = ds['elevation'].values  # (time, node)
    elev[:, idmask == 1] = 0.0

    ds['elevation'].values[:] = elev
    ds['elevation'].attrs.pop('missing_value', None)

    ds = ds.assign_coords(nSCHISM_hgrid_edge=np.arange(7791537))
    ds = ds.assign_coords(nSCHISM_vgrid_layers=np.arange(49))
    ds = ds.assign_coords(two=np.arange(2))

    ds.to_netcdf(filename_o)
    return()

if __name__ == "__main__":
    filename_is = ['stofs_3d_atl.t12z.fields.out2d_forecast_day1.nc']
    filename_os = ['out2d_1.nc']

    add_variables(filename_is, filename_os)


