import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def pannel_obs_sim_analyst(series, freq, params, fld_obs='Obs', fld_sim='Sim', fld_date='Date', filename='analyst', suff='',
                           folder='C:/bin', show=False, log=True, units='flow', title='Obs/Sim Analysis'):
    """
    Pannel of Obs vs. Sim Analyst
    :param series: Series Analyst dataframe (from obs_sim_analyst() function in tools.py)
    :param freq: Frequency Analyst dataframe (from obs_sim_analyst() function in tools.py)
    :param params: Parameters Analyst dataframe
    :param fld_obs: string of field of observed series data
    :param fld_sim: string of field of simulated series data
    :param fld_date: string of date field
    :param filename: string of file name
    :param suff: optional string for suffix
    :param folder: string of export directory
    :param show: boolean to control showing figure
    :return: string of file
    """
    #
    fig = plt.figure(figsize=(18, 9))  # Width, Height
    gs = mpl.gridspec.GridSpec(5, 13, wspace=0.9, hspace=0.9)
    fig.suptitle(title)
    if units == 'flow':
        units = 'mm/d'
    elif units == 'stock':
        units = 'mm'
    #
    # min max setup
    vmax = np.max((np.max(series[fld_obs]), np.max(series[fld_sim])))
    vmin = np.min((np.min(series[fld_obs]), np.min(series[fld_sim])))
    #
    # plot of CFCs
    plt.subplot(gs[0:2, 0:2])
    plt.title('CFCs', loc='left')
    plt.plot(freq['Exeedance'], freq['ValuesObs'], 'tab:grey', label='Obs')
    plt.plot(freq['Exeedance'], freq['ValuesSim'], 'tab:blue', label='Sim')
    plt.ylim((vmin, 1.2 * vmax))
    if log:
        plt.yscale('log')
    plt.ylabel(units)
    plt.xlabel('Exeed. %')
    plt.grid(True)
    plt.legend(loc='upper right')
    #
    # plot of series
    plt.subplot(gs[0:2, 3:10])
    plt.title('Series', loc='left')
    plt.plot(series[fld_date], series[fld_obs], 'tab:grey', linewidth=2, label='Observed')
    plt.plot(series[fld_date], series[fld_sim], 'tab:blue', label='Simulated')
    plt.ylim((vmin, 1.2 * vmax))
    if log:
        plt.yscale('log')
    plt.ylabel(units)
    plt.grid(True)
    plt.legend(loc='upper right', ncol=2)
    #
    # plot of Scatter
    plt.subplot(gs[0:2, 11:])
    plt.title('Obs vs. Sim  (R={:.2f})'.format(float(params[params['Parameter'] == 'R']['Value'])), loc='left')
    plt.scatter(series[fld_obs], series[fld_sim], c='tab:grey', s=15, alpha=0.3, edgecolors='none')
    plt.xlabel('Obs  ({})'.format(units))
    plt.ylabel('Sim  ({})'.format(units))
    if log:
        plt.xscale('log')
        plt.yscale('log')
    plt.plot([0, vmax], [0, vmax], 'tab:grey', linestyle='--', label='1:1')
    plt.ylim((vmin, 1.2 * vmax))
    plt.xlim((vmin, 1.2 * vmax))
    plt.grid(True)
    plt.legend(loc='upper left')
    #
    # plot of CFC Erros
    plt.subplot(gs[2, 0:2])
    plt.title('CFC Error', loc='left')
    plt.plot(freq['Exeedance'], freq['E'], 'tab:red')
    plt.ylabel(units)
    plt.xlabel('Exeed. %')
    plt.grid(True)
    #
    # plot Error
    plt.subplot(gs[2, 3:10])
    plt.title('Series - Error', loc='left')
    plt.plot(series[fld_date], series['E'], 'tab:red')
    plt.ylabel(units)
    plt.grid(True)
    #
    # plot
    plt.subplot(gs[3, 0:2])
    plt.title('CFC - Squared Error', loc='left')
    plt.plot(freq['Exeedance'], freq['SE'], 'tab:red')
    plt.xlabel('Exeed. %')
    plt.grid(True)
    #
    # plot
    plt.subplot(gs[3, 3:10])
    plt.title('Series - Sq. Error', loc='left')
    plt.plot(series[fld_date], series['SE'], 'tab:red')
    plt.grid(True)
    #
    plt.subplot(gs[3, 11:])
    plt.title('Analyst parameters', loc='left')
    plt.text(x=0, y=0.8,  s='Pbias : {:.2f}%'.format(float(params[params['Parameter'] == 'PBias']['Value'])))
    plt.text(x=0, y=0.6,  s='R : {:.2f}'.format(float(params[params['Parameter'] == 'R']['Value'])))
    plt.text(x=0, y=0.4,  s='RMSE : {:.2f} mm'.format(float(params[params['Parameter'] == 'RMSE']['Value'])))
    plt.text(x=0, y=0.2,  s='NSE : {:.2f}'.format(float(params[params['Parameter'] == 'NSE']['Value'])))
    plt.text(x=0, y=0.0,  s='KGE : {:.2f}'.format(float(params[params['Parameter'] == 'KGE']['Value'])))
    if log:
        plt.text(x=0, y=-0.2, s='KGElog : {:.2f}'.format(float(params[params['Parameter'] == 'KGElog']['Value'])))
        plt.text(x=0, y=-0.4, s='RMSElog : {:.2f}'.format(float(params[params['Parameter'] == 'RMSElog']['Value'])))
        plt.text(x=0, y=-0.6, s='NSElog : {:.2f}'.format(float(params[params['Parameter'] == 'NSElog']['Value'])))
    plt.text(x=0, y=-1.0, s='CFC-R : {:.2f}'.format(float(params[params['Parameter'] == 'R-CFC']['Value'])))
    plt.text(x=0, y=-1.2, s='CFC-RMSE : {:.2f}'.format(float(params[params['Parameter'] == 'RMSE-CFC']['Value'])))
    if log:
        plt.text(x=0, y=-1.4, s='CFC-RMSElog : {:.2f}'.format(float(params[params['Parameter'] == 'RMSElog-CFC']['Value'])))
    plt.axis('off')
    #
    if log:
        # plot
        plt.subplot(gs[4, 0:2])
        plt.title('CFC - Sq. Error of Log', loc='left')
        plt.plot(freq['Exeedance'], freq['SElog'], 'tab:red')
        plt.xlabel('Exeed. %')
        plt.grid(True)
        # plot
        plt.subplot(gs[4, 3:10])
        plt.title('Series - Sq. Error of Log', loc='left')
        plt.plot(series[fld_date], series['SElog'], 'tab:red')
        plt.grid(True)
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        if suff != '':
            filepath = folder + '/' + filename + '_' + suff + '.png'
        else:
            filepath = folder + '/' + filename + '.png'
        plt.savefig(filepath)
        plt.close(fig)
        return filepath


def pannel_calib_valid(series_full, series_calib, series_valid, freq_full, params_full, params_calib, params_valid,
                       fld_obs='Obs', fld_sim='Sim', fld_date='Date',
                       filename='analyst_CVF', suff='', folder='C:/bin',
                       show=False, log=True, units='flow', title='Obs/Sim Analysis'):
    """

    Plot Calibration/Validation/Full Pannel - CVF Analyst

    :param series_full: pandas dataframe
    :param series_calib: pandas dataframe
    :param series_valid: pandas dataframe
    :param freq_full: pandas dataframe
    :param params_full: pandas dataframe
    :param params_calib: pandas dataframe
    :param params_valid: pandas dataframe
    :param fld_obs: string of field of OBS
    :param fld_sim: string of field of SIM
    :param fld_date: string of field of Date or X axis
    :param filename: string of filename
    :param suff: string suffix
    :param folder: string to foldepath
    :param show: boolean to show instead of save
    :param log: boolean to log scale
    :param units: string of units type. Options: 'flow' or 'stock'
    :param title: string of superior title
    :return: string of filepath
    """
    #
    fig = plt.figure(figsize=(18, 9))  # Width, Height
    gs = mpl.gridspec.GridSpec(5, 13, wspace=0.9, hspace=0.9)
    fig.suptitle(title)
    if units == 'flow':
        units = 'mm/d'
    elif units == 'stock':
        units = 'mm'
    #
    # min max setup
    vmax = np.max((np.max(series_full[fld_obs]), np.max(series_full[fld_sim])))
    vmin = np.min((np.min(series_full[fld_obs]), np.min(series_full[fld_sim])))
    #
    # plot of CFCs
    plt.subplot(gs[0:2, 0:2])
    plt.title('CFCs - Full', loc='left')
    plt.plot(freq_full['Exeedance'], freq_full['ValuesObs'], 'tab:grey', label='Obs.')
    plt.plot(freq_full['Exeedance'], freq_full['ValuesSim'], 'blue', label='Sim.')
    plt.ylim((vmin, 1.2 * vmax))
    if log:
        plt.yscale('log')
    plt.ylabel(units)
    plt.xlabel('Exeed. %')
    plt.grid(True)
    plt.legend(loc='upper right')
    #
    # plot of series
    plt.subplot(gs[0:2, 3:10])
    plt.title('Series', loc='left')
    plt.plot(series_full[fld_date], series_full[fld_obs], 'tab:grey', linewidth=2, label='Observed')
    plt.plot(series_calib[fld_date], series_calib[fld_sim], 'tab:blue', label='Calibration')
    plt.plot(series_valid[fld_date], series_valid[fld_sim], 'navy', label='Validation')
    plt.ylim((vmin, 1.5 * vmax))
    if log:
        plt.yscale('log')
    plt.ylabel(units)
    plt.grid(True)
    plt.legend(loc='upper right', ncol=3)
    #
    # plot of Scatter
    plt.subplot(gs[0:2, 11:])
    params = params_full
    plt.title('Obs vs. Sim  (R={:.2f})'.format(float(params[params['Parameter'] == 'R']['Value'])), loc='left')
    plt.scatter(series_calib[fld_obs], series_calib[fld_sim], c='tab:blue', s=15, alpha=0.3, edgecolors='none', label='Calib.')
    plt.scatter(series_valid[fld_obs], series_valid[fld_sim], c='navy', s=15, alpha=0.6, edgecolors='none', label='Valid.')
    plt.xlabel('Obs  ({})'.format(units))
    plt.ylabel('Sim  ({})'.format(units))
    if log:
        plt.xscale('log')
        plt.yscale('log')
    plt.plot([0, vmax], [0, vmax], 'tab:grey', linestyle='--', label='1:1')
    plt.ylim((vmin, 1.2 * vmax))
    plt.xlim((vmin, 1.2 * vmax))
    plt.grid(True)
    plt.legend(loc='upper left')
    #
    # plot of CFC Erros
    plt.subplot(gs[2, 0:2])
    plt.title('CFC Error', loc='left')
    plt.plot(freq_full['Exeedance'], freq_full['E'], 'tab:red')
    plt.ylabel(units)
    plt.xlabel('Exeed. %')
    plt.grid(True)
    #
    # plot Error
    plt.subplot(gs[2, 3:10])
    plt.title('Series - Error', loc='left')
    plt.plot(series_calib[fld_date], series_calib['E'], 'tab:red')
    plt.plot(series_valid[fld_date], series_valid['E'], 'maroon')
    plt.ylabel(units)
    plt.grid(True)
    #
    # plot
    plt.subplot(gs[3, 0:2])
    plt.title('CFC - Squared Error', loc='left')
    plt.plot(freq_full['Exeedance'], freq_full['SE'], 'tab:red')
    plt.xlabel('Exeed. %')
    plt.grid(True)
    #
    # plot
    plt.subplot(gs[3, 3:10])
    plt.title('Series - Sq. Error', loc='left')
    plt.plot(series_calib[fld_date], series_calib['SE'], 'tab:red')
    plt.plot(series_valid[fld_date], series_valid['SE'], 'maroon')
    plt.grid(True)
    #
    plt.subplot(gs[3, 11:])
    plt.title('Analyst parameters', loc='left')
    subtls = ['Full', 'Calib.', 'Valid.']
    all_params = [params_full, params_calib, params_valid]
    xs = [-0.8, 0.15, 1.1]
    for i in range(len(subtls)):
        params = all_params[i]
        plt.text(x=xs[i], y=0.8, s='{}'.format(subtls[i]))
        plt.text(x=xs[i], y=0.6, s='Pbias : {:.2f}%'.format(float(params[params['Parameter'] == 'PBias']['Value'])))
        plt.text(x=xs[i], y=0.4, s='R : {:.2f}'.format(float(params[params['Parameter'] == 'R']['Value'])))
        plt.text(x=xs[i], y=0.2, s='RMSE : {:.2f} mm'.format(float(params[params['Parameter'] == 'RMSE']['Value'])))
        plt.text(x=xs[i], y=0.0, s='NSE : {:.2f}'.format(float(params[params['Parameter'] == 'NSE']['Value'])))
        plt.text(x=xs[i], y=-0.2, s='KGE : {:.2f}'.format(float(params[params['Parameter'] == 'KGE']['Value'])))
        if log:
            plt.text(x=xs[i], y=-0.4, s='KGElog : {:.2f}'.format(float(params[params['Parameter'] == 'KGElog']['Value'])))
            plt.text(x=xs[i], y=-0.6, s='RMSElog : {:.2f}'.format(float(params[params['Parameter'] == 'RMSElog']['Value'])))
            plt.text(x=xs[i], y=-0.8, s='NSElog : {:.2f}'.format(float(params[params['Parameter'] == 'NSElog']['Value'])))
        if subtls[i] == 'Full':
            plt.text(x=xs[i], y=-1.2, s='CFC-R : {:.2f}'.format(float(params[params['Parameter'] == 'R-CFC']['Value'])))
            plt.text(x=xs[i], y=-1.4, s='CFC-RMSE : {:.2f}'.format(float(params[params['Parameter'] == 'RMSE-CFC']['Value'])))
            if log:
                plt.text(x=xs[i], y=-1.6,
                         s='CFC-RMSElog : {:.2f}'.format(float(params[params['Parameter'] == 'RMSElog-CFC']['Value'])))
    plt.axis('off')
    #
    if log:
        # plot
        plt.subplot(gs[4, 0:2])
        plt.title('CFC - Sq. Error of Log', loc='left')
        plt.plot(freq_full['Exeedance'], freq_full['SElog'], 'tab:red')
        plt.xlabel('Exeed. %')
        plt.grid(True)
        # plot
        plt.subplot(gs[4, 3:10])
        plt.title('Series - Sq. Error of Log', loc='left')
        plt.plot(series_calib[fld_date], series_calib['SElog'], 'tab:red')
        plt.plot(series_valid[fld_date], series_valid['SElog'], 'maroon')
        plt.grid(True)
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        if suff != '':
            filepath = folder + '/' + filename + '_' + suff + '.png'
        else:
            filepath = folder + '/' + filename + '.png'
        plt.savefig(filepath)
        plt.close(fig)
        return filepath


def pannel_local(series, star, deficit, sups, mids, star_rng, deficit_rng,
                 sup1_rng, sup2_rng, sup3_rng, sup4_rng,
                 mid1_rng, mid2_rng, mid3_rng, mid4_rng,
                 t, offset_back, offset_front, type='ET', filename='frame', folder='C:/bin',
                 show=False, suff='', dpi=300, png=True):
    """

    Plot the local pannel frame

    :param series: pandas dataframe
    :param star: 2d numpy array of Star map
    :param deficit: 2d numpy array of Deficit
    :param sups: 3d numpy array of superior 2d numpy arrays maps
    :param mids: 3d numpy array of median 2d numpy arrays maps
    :param star_rng: iterable of star range
    :param deficit_rng: iterable of map range
    :param sup1_rng: iterable of map range
    :param sup2_rng: iterable of map range
    :param sup3_rng: iterable of map range
    :param sup4_rng: iterable of map range
    :param mid1_rng: iterable of map range
    :param mid2_rng: iterable of map range
    :param mid3_rng: iterable of map range
    :param mid4_rng: iterable of map range
    :param t: integer time step
    :param offset_back: int offset to back window
    :param offset_front: int offset to front window
    :param type: string - type of pannel - ET, Qv, R.
    :param filename: string filename
    :param folder: string folder path
    :param show: boolean to show instead of save
    :param suff: string suffix
    :param dpi: boolean
    :param png: boolean
    :return: string filepath
    """
    from matplotlib import cm
    from matplotlib.colors import ListedColormap
    from pandas import to_datetime
    #
    #
    earth_big = cm.get_cmap('gist_earth_r', 512)
    earthcm = ListedColormap(earth_big(np.linspace(0.10, 0.95, 256)))
    jet_big = cm.get_cmap('jet_r', 512)
    jetcm = ListedColormap(jet_big(np.linspace(0.3, 0.75, 256)))
    jet_big2 = cm.get_cmap('jet', 512)
    jetcm2 = ListedColormap(jet_big2(np.linspace(0.1, 0.9, 256)))
    viridis_big = cm.get_cmap('viridis_r', 512)
    viridiscm = ListedColormap(viridis_big(np.linspace(0.05, 0.9)))
    #
    dates_labels = to_datetime(series['Date'], format='%Y%m%d')
    dates_labels = dates_labels.astype('str')
    #
    #
    if type == 'ET':
        cmaps = (jetcm, jetcm2, 'Blues', 'BuPu', 'BuPu', 'BuPu', jetcm, jetcm, jetcm, jetcm)
        titles = ('ET - Evapotranspiration (mm/d)',
                  'Groundwater\ndeficit (mm)',
                  'Precipitation\n(mm/d)',
                  'Irrigation by\naspersion (mm/d)',
                  'Irrigation by\ninundation (mm/d)',
                  'Total irrigation\ninput (mm/d)',
                  'Evaporation\nfrom canopy (mm/d)', 'Evaporation\nfrom surface (mm/d)',
                  'Transpiration\nfrom soil (mm/d)', 'Transpiration from\ngroundwater (mm/d)')
        suptitle = 'Evapotranspiration (ET) Pannel | {}'.format(dates_labels.values[t])
        series_label = 'ET & PET.\nmm/d'
        lengend_lbl = 'ET'
        star_color = 'tab:red'
    elif type == 'Qv':
        cmaps = (earthcm, jetcm2, 'Blues', 'BuPu', 'BuPu', 'BuPu', earthcm, viridiscm, viridiscm, viridiscm)
        titles = ('Recharge (mm/d)',
                  'Groundwater\ndeficit (mm)',
                  'Precipitation\n(mm/d)',
                  'Irrigation by\naspersion (mm/d)',
                  'Irrigation by\ninundation (mm/d)',
                  'Total irrigation\ninput (mm/d)',
                  'Infiltration\n(mm/d)', 'Canopy\nwater stock (mm)',
                  'Surface\nwater stock (mm)', 'Soil\nwater stock (mm)')
        suptitle = 'Recharge to groundwater Pannel | {}'.format(dates_labels.values[t])
        series_label = 'Recharge\nmm/d'
        star_color = 'teal'
        lengend_lbl = 'Recharge'
    elif type == 'R':
        cmaps = (earthcm, jetcm2, 'Blues', 'BuPu', 'BuPu', 'BuPu', earthcm, earthcm, earthcm, 'Blues')
        titles = ('Runoff (mm/d)',
                  'Groundwater\ndeficit (mm)',
                  'Precipitation\n(mm/d)',
                  'Irrigation by\naspersion (mm/d)',
                  'Irrigation by\ninundation (mm/d)',
                  'Total irrigation\ninput (mm/d)',
                  'Throughfall\n(mm/d)', 'Infiltration excess\nrunoff (mm/d)',
                  'Saturation excess\nrunoff (mm/d)', 'Variable\nSource Area')
        suptitle = 'Runoff Pannel | {}'.format(dates_labels.values[t])
        series_label = 'Runoff\nmm/d'
        lengend_lbl = 'Runoff'
        star_color = 'blue'
    #
    # Star plot
    fig = plt.figure(figsize=(17, 8))  # Width, Height
    gs = mpl.gridspec.GridSpec(8, 17, wspace=0.8, hspace=0.6)
    fig.suptitle(suptitle)
    #
    # STAR
    plt.subplot(gs[:5, :5])
    im = plt.imshow(star, cmap=cmaps[0], vmin=star_rng[0], vmax=star_rng[1])
    plt.title(titles[0])
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # DEFICIT
    plt.subplot(gs[5:, :3])
    im = plt.imshow(deficit, cmap=cmaps[1], vmin=deficit_rng[0], vmax=deficit_rng[1])
    plt.title(titles[1], fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # SUP 1 - Prec
    lcl_rng = sup1_rng
    prec_map = (sups[0] * 0.0) + series['Prec'].values[t]
    plt.subplot(gs[:2, 5:7])
    im = plt.imshow(prec_map, cmap=cmaps[2], vmin=lcl_rng[0], vmax=lcl_rng[1])
    plt.title(titles[2], fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    # SUP 2 - IRA
    lcl_rng = sup2_rng
    plt.subplot(gs[:2, 8:10])
    im = plt.imshow(sups[0], cmap=cmaps[3], vmin=lcl_rng[0], vmax=lcl_rng[1])
    plt.title(titles[3], fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    # SUP 3
    lcl_rng = sup3_rng
    plt.subplot(gs[:2, 11:13])
    im = plt.imshow(sups[1], cmap=cmaps[4], vmin=lcl_rng[0], vmax=lcl_rng[1])
    plt.title(titles[4], fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    # SUP 4
    lcl_rng = sup4_rng
    plt.subplot(gs[:2, 14:16])
    im = plt.imshow(sups[0] + sups[1], cmap=cmaps[5], vmin=lcl_rng[0], vmax=lcl_rng[1])
    plt.title(titles[5], fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    #
    # MID 1
    lcl_rng = mid1_rng
    plt.subplot(gs[2:5, 5:8])
    im = plt.imshow(mids[0], cmap=cmaps[6], vmin=lcl_rng[0], vmax=lcl_rng[1])
    plt.title(titles[6], fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    # MID 2
    lcl_rng = mid2_rng
    plt.subplot(gs[2:5, 8:11])
    im = plt.imshow(mids[1], cmap=cmaps[7], vmin=lcl_rng[0], vmax=lcl_rng[1])
    plt.title(titles[7], fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    # MID 3
    lcl_rng = mid3_rng
    plt.subplot(gs[2:5, 11:14])
    im = plt.imshow(mids[2], cmap=cmaps[8], vmin=lcl_rng[0], vmax=lcl_rng[1])
    plt.title(titles[8], fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    # MID 4
    lcl_rng = mid4_rng
    plt.subplot(gs[2:5, 14:])
    im = plt.imshow(mids[3], cmap=cmaps[9], vmin=lcl_rng[0], vmax=lcl_rng[1])
    plt.title(titles[9], fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # SERIES
    #
    if t < offset_back:
        low = 0
        hi = offset_front + offset_back + 1
    elif t >= len(series) - offset_front - 1:
        low = len(series) - offset_front - offset_back - 1
        hi = len(series)
    else:
        low = t - offset_back
        hi = t + offset_front + 1
    #
    #
    #
    # Input water
    ax = fig.add_subplot(gs[5, 5:])
    plt.title('Date: {}'.format(dates_labels.values[t]), loc='left', fontsize=10)
    plt.vlines(series['Date'].values[t], ymax=1.5 * np.max(series['Prec'].values), ymin=0, colors=['k'])
    plt.plot(series['Date'].values[low:hi],
             series['Prec'].values[low:hi], 'tab:blue', label='Precip.')
    plt.legend(loc='upper left', ncol=1, framealpha=1, fancybox=False)
    plt.ylim((0, 1.5 * np.max(series['Prec'].values)))
    # markers
    plt.plot(series['Date'].values[t], series['Prec'].values[t], 'o', color='tab:blue')
    # IRA and IRI
    ax2 = ax.twinx()
    plt.plot(series['Date'].values[low:hi],
             series['IRA'].values[low:hi], 'green', label='IRA')
    plt.plot(series['Date'].values[low:hi],
             series['IRI'].values[low:hi], 'orange', label='IRI')
    plt.ylim((0, 1.5 * np.max((series['IRA'].values, series['IRI'].values))))
    # markers
    plt.plot(series['Date'].values[t], series['IRA'].values[t], 'o', color='green')
    plt.plot(series['Date'].values[t], series['IRI'].values[t], 'o', color='orange')
    #
    # legend
    plt.legend(loc='upper right', ncol=2, framealpha=1, fancybox=False)
    fig.text(x=0.28, y=0.33, s='Precip.\nmm/d')
    fig.text(x=0.93, y=0.33, s='Irrigation\nmm/d')
    #
    #
    #
    # star plot
    ax = fig.add_subplot(gs[6, 5:])
    if type == 'ET':
        plt.plot(series['Date'].values[low:hi],
             series['PET'].values[low:hi], 'tab:grey', label='PET')
    plt.plot(series['Date'].values[low:hi],
             series[type].values[low:hi], color=star_color, label=lengend_lbl)
    plt.vlines(series['Date'].values[t], ymax=1.5 * np.max(series[type].values), ymin=0, colors=['k'])
    plt.plot(series['Date'].values[t], series[type].values[t], 'o', color=star_color)
    plt.ylim((0, 1.5 * np.max(series[type])))
    plt.legend(loc='upper right', ncol=2, framealpha=1, fancybox=False)
    fig.text(x=0.28, y=0.23, s=series_label)
    #
    #
    #
    # Flow
    ax = fig.add_subplot(gs[7, 5:])
    plt.plot(series['Date'].values[low:hi],
             series['Q'].values[low:hi], 'tab:blue', label='Flow')
    plt.plot(series['Date'].values[low:hi],
             series['Qb'].values[low:hi], 'navy', label='Baseflow')
    plt.vlines(series['Date'].values[t], ymax= 10 * np.max(series['Q'].values), ymin=np.min(series['Q'].values),
               colors=['k'])
    if series['Q'].values[t] == series['Qb'].values[t]:
        plt.plot(series['Date'].values[t], series['Q'].values[t], 'o', color='navy')
    else:
        plt.plot(series['Date'].values[t], series['Q'].values[t], 'o', color='tab:blue')
        plt.plot(series['Date'].values[t], series['Qb'].values[t], 'o', color='navy')
    plt.ylim((np.min(series['Q']), 10 * np.max(series['Q'])))
    plt.legend(loc='upper right', ncol=2, framealpha=1, fancybox=False)
    plt.yscale('log')
    fig.text(x=0.28, y=0.13, s='Flow\nmm/d')
    #
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        if suff != '':
            filepath = '{}/{}_{}_{}_{}'.format(folder, suff, filename, type, dates_labels.values[t])
        else:
            filepath = '{}/{}_{}_{}'.format(folder, filename, type, dates_labels.values[t])
        if png:
            filepath = filepath + '.png'
        else:
            filepath = filepath + '.jpg'
        plt.savefig(filepath, dpi=dpi)
        plt.close(fig)
        plt.clf()
        return filepath


def pannel_prec_q(t, prec, q, grid=True, folder='C:/bin', filename='pannel_prec_q', suff='', show=False):
    """

    A simple Prec/Q plot

    :param t: iterable of dates/timestep
    :param prec: iterable of Prec
    :param q: iterable of Q
    :param grid: boolean to grid
    :param folder: string to folder path
    :param filename: string of filename
    :param suff: string of suffix
    :param show: boolean to show instead of saving
    :return: string filepath
    """
    #
    fig = plt.figure(figsize=(16, 8))  # Width, Height
    gs = mpl.gridspec.GridSpec(2, 1, wspace=0.8, hspace=0.6)
    # plot prec
    y = prec
    ymax = np.max(y)
    ax1 = fig.add_subplot(gs[0, 0])
    plt.title('Precipitation', loc='left')
    plt.ylabel('mm/d')
    plt.plot(t, y)
    plt.ylim(0, 1.1 * ymax)
    plt.grid(grid)
    #plt.xticks(locs, labels)
    # plot q
    y = q
    ymax = np.max(y)
    ax2 = fig.add_subplot(gs[1, 0], sharex=ax1)
    plt.title('Flow', loc='left')
    plt.ylabel('mm/d')
    plt.plot(t, y)
    plt.ylim(0, 1.1 * ymax)
    plt.grid(grid)
    #plt.xticks(locs, labels)
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        filepath = folder + '/' + filename + '_' + suff + '.png'
        plt.savefig(filepath)
        plt.close(fig)
        return filepath


def pannel_prec_q_logq(t, prec, q, grid=True, folder='C:/bin', filename='pannel_prec_q_logq', suff='', show=False):
    """

    A simple Prec/Q plot but with also the Log Q

    :param t: iterable of dates/timestep
    :param prec: iterable of Prec
    :param q: iterable of Q
    :param grid: boolean to grid
    :param folder: string to folder path
    :param filename: string of filename
    :param suff: string of suffix
    :param show: boolean to show instead of saving
    :return: string filepath
    """
    #
    fig = plt.figure(figsize=(16, 8))  # Width, Height
    gs = mpl.gridspec.GridSpec(3, 1, wspace=0.8, hspace=0.6)
    # plot prec
    y = prec
    ymax = np.max(y)
    ax1 = fig.add_subplot(gs[0, 0])
    plt.title('Precipitation', loc='left')
    plt.ylabel('mm/d')
    plt.plot(t, y)
    plt.ylim(0, 1.1 * ymax)
    plt.grid(grid)
    # plot q
    y = q
    ymax = np.max(y)
    ax2 = fig.add_subplot(gs[1, 0], sharex=ax1)
    plt.title('Flow', loc='left')
    plt.ylabel('mm/d')
    plt.plot(t, y)
    plt.ylim(0, 1.1 * ymax)
    plt.grid(grid)
    # plot log q
    y = q
    ymax = np.max(y)
    ymin = np.min(y)
    ax3 = fig.add_subplot(gs[2, 0], sharex=ax1)
    plt.title('Flow', loc='left')
    plt.ylabel('mm/d')
    plt.plot(t, y)
    plt.ylim(0.9 * ymin, 1.1 * ymax)
    plt.yscale('log')
    plt.grid(grid)
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        filepath = folder + '/' + filename + '_' + suff + '.png'
        plt.savefig(filepath)
        plt.close(fig)
        return filepath


def pannel_sim_prec_q_logq(t, prec, qobs, qsim, grid=True, folder='C:/bin', filename='pannel_sim_prec_q_logq', suff='', show=False):
    """

    Plot a Pannel of Qsim and Qobs in linear and log scale

    :param t: iterable of dates/timestep
    :param prec: iterable of Prec
    :param qobs: iterable of QOBS
    :param qsim: iterable of QSIM
    :param grid: boolean to grid
    :param folder: string to folder path
    :param filename: string of filename
    :param suff: string of suffix
    :param show: boolean to show instead of saving
    :return:
    """
    fig = plt.figure(figsize=(16, 8))  # Width, Height
    gs = mpl.gridspec.GridSpec(3, 1, wspace=0.8, hspace=0.6)
    # plot prec
    y = prec
    ymax = np.max(y)
    ax1 = fig.add_subplot(gs[0, 0])
    plt.title('Precipitation', loc='left')
    plt.ylabel('mm/d')
    plt.plot(t, y)
    plt.ylim(0, 1.1 * ymax)
    plt.grid(grid)
    # plot q
    y1 = qobs
    y2 = qsim
    ymax = np.max((y1, y2))
    ax2 = fig.add_subplot(gs[1, 0], sharex=ax1)
    plt.title('Flow', loc='left')
    plt.ylabel('mm/d')
    plt.plot(t, y1)
    plt.plot(t, y2)
    plt.ylim(0, 1.1 * ymax)
    plt.grid(grid)
    # plot log q
    ymin = np.min((y1, y2))
    ax3 = fig.add_subplot(gs[2, 0], sharex=ax1)
    plt.title('FLow', loc='left')
    plt.ylabel('mm/d')
    plt.plot(t, y1)
    plt.plot(t, y2)
    plt.ylim(0.9 * ymin, 1.1 * ymax)
    plt.yscale('log')
    plt.grid(grid)
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        filepath = folder + '/' + filename + '_' + suff + '.png'
        plt.savefig(filepath)
        plt.close(fig)
        return filepath


def pannel_global(dataframe, qobs=False, grid=True, show=False, folder='C:/bin', filename='pannel_topmodel', suff=''):
    """
    visualize the topmodel global variables in a single pannel
    :param dataframe: pandas dataframe from hydrology.topmodel_sim()
    :param grid: boolean for grid
    :param folder: string to destination directory
    :param filename: string file name
    :param suff: string suffix in file name
    :param show: boolean control to show figure instead of saving it
    :return: string file path
    """
    #
    fig = plt.figure(figsize=(20, 12))  # Width, Height
    fig.suptitle('Pannel of simulated hydrological processes')
    gs = mpl.gridspec.GridSpec(5, 18, wspace=0.0, hspace=0.2)  # nrows, ncols
    col1 = 8
    col2 = 10
    max_prec = 1.2 * np.max(dataframe['Prec'].values)
    max_et = 1.2 * np.max(dataframe['PET'].values)
    max_irr = 1.5 * np.max((dataframe['IRI'].values, dataframe['IRA'].values))
    if max_irr == 0:
        max_irr = 1
    max_stocks = 1.2 * np.max((dataframe['Unz'].values, dataframe['Sfs'].values, dataframe['Cpy'].values))
    max_int_flow = 1.2 * np.max((dataframe['Inf'].values, dataframe['Qv'].values))
    qmin = 0.8 * np.min(dataframe['Q'].values)
    if qobs:
        qmin = 0.8 * np.min((dataframe['Q'].values, dataframe['Qobs'].values))
    # 1
    ax = fig.add_subplot(gs[0, 0:col1])
    plt.grid(grid)
    plt.plot(dataframe['Date'], dataframe['Prec'], label='Precipitation')
    plt.ylabel('mm/d (Prec)')
    plt.ylim(0, max_prec)
    plt.legend(loc='upper left', ncol=1, framealpha=1, fancybox=False)
    ax2 = ax.twinx()
    plt.plot(dataframe['Date'], dataframe['IRA'], 'orange', label='Irrigation by aspersion')
    plt.plot(dataframe['Date'], dataframe['IRI'], 'green', label='Irrigation by inundation')
    plt.ylabel('mm/d (IRA, IRI)')
    plt.ylim(0, max_irr)
    plt.legend(loc='upper right', ncol=2, framealpha=1, fancybox=False)
    ax.tick_params(axis='x', which='major', labelsize=8)
    # 1
    ax = fig.add_subplot(gs[0, col2:])
    plt.grid(grid)
    plt.plot(dataframe['Date'], dataframe['Temp'], 'tab:orange', label='Temperature')
    plt.ylabel('°C')
    plt.legend(loc='upper left', ncol=1, framealpha=1, fancybox=False)
    ax2 = ax.twinx()
    plt.plot(dataframe['Date'], dataframe['PET'], 'tab:grey', label='PET - Potential Evapotranspiration')
    plt.ylim(0, max_et)
    plt.ylabel('mm/d')
    plt.legend(loc='upper right', ncol=1, framealpha=1, fancybox=False)
    ax.tick_params(axis='x', which='major', labelsize=8)
    # 2
    ax = fig.add_subplot(gs[1, 0:col1])
    plt.grid(grid)
    plt.plot(dataframe['Date'], dataframe['TF'], 'skyblue', label='Troughfall')
    plt.plot(dataframe['Date'], dataframe['R'], 'dodgerblue', label='Runoff')
    plt.plot(dataframe['Date'], dataframe['RIE'], 'blue', label='Hortonian R.')
    plt.plot(dataframe['Date'], dataframe['RSE'], 'navy', label='Dunnean R.')
    plt.ylabel('mm/d')
    plt.ylim(0, max_prec)
    plt.legend(loc='upper left', ncol=4, framealpha=1, fancybox=False)
    ax.tick_params(axis='x', which='major', labelsize=8)
    # 3
    ax = fig.add_subplot(gs[1, col2:])
    plt.grid(grid)
    plt.plot(dataframe['Date'], dataframe['PET'], 'tab:grey', label='PET')
    plt.plot(dataframe['Date'], dataframe['ET'], 'tab:red', label='Actual ET')
    plt.ylim(0, max_et)
    plt.ylabel('mm/d')
    plt.legend(loc='upper right', ncol=2, framealpha=1, fancybox=False)
    ax.tick_params(axis='x', which='major', labelsize=8)
    # 3
    ax = fig.add_subplot(gs[2, 0:col1])
    plt.grid(grid)
    if qobs:
        plt.plot(dataframe['Date'], dataframe['Qobs'], 'tab:grey', label='Observed data')
    plt.plot(dataframe['Date'], dataframe['Q'], 'tab:blue', label='Flow')
    plt.plot(dataframe['Date'], dataframe['Qb'], 'navy', label='Baseflow')
    plt.ylim(qmin, 10 * max_prec)
    plt.ylabel('mm/d')
    plt.legend(loc='upper right', ncol=3, framealpha=1, fancybox=False)
    ax.tick_params(axis='x', which='major', labelsize=8)
    plt.yscale('log')

    # 3
    ax = fig.add_subplot(gs[2, col2:])
    plt.grid(grid)
    plt.plot(dataframe['Date'], dataframe['PET'], 'tab:grey', label='PET')
    plt.plot(dataframe['Date'], dataframe['Evc'], 'tan', label='Evap. canopy')
    plt.plot(dataframe['Date'], dataframe['Evs'], 'maroon', label='Evap. surface')
    plt.ylim(0, max_et)
    plt.ylabel('mm/d')
    plt.legend(loc='upper right', ncol=3, framealpha=1, fancybox=False)
    ax.tick_params(axis='x', which='major', labelsize=8)
    # 3
    ax = fig.add_subplot(gs[3, 0:col1])
    plt.grid(grid)
    plt.plot(dataframe['Date'], dataframe['Inf'], 'tab:blue', label='Infiltration')
    plt.plot(dataframe['Date'], dataframe['Qv'], 'navy', label='Groundwater recharge')
    plt.ylim(0, max_int_flow)
    plt.ylabel('mm/d')
    plt.legend(loc='upper left', ncol=2, framealpha=1, fancybox=False)
    # 3
    ax = fig.add_subplot(gs[3, col2:])
    plt.grid(grid)
    plt.plot(dataframe['Date'], dataframe['PET'], 'tab:grey', label='PET')
    plt.plot(dataframe['Date'], dataframe['Tpun'], 'yellowgreen', label='Transp. vadose zone')
    plt.plot(dataframe['Date'], dataframe['Tpgw'], 'darkgreen', label='Transp. groundwater')
    plt.ylim(0, max_et)
    plt.ylabel('mm/d')
    plt.legend(loc='upper right', ncol=3, framealpha=1, fancybox=False)
    ax.tick_params(axis='x', which='major', labelsize=8)
    # 3
    ax = fig.add_subplot(gs[4, 0:col1])
    plt.grid(grid)
    plt.plot(dataframe['Date'], dataframe['D'], 'k', label='Groundwater stock deficit')
    plt.ylim(0, 1.5 * np.max(dataframe['D'].values))
    plt.ylabel('mm')
    plt.legend(loc='upper left', ncol=2, framealpha=1, fancybox=False)
    ax2 = ax.twinx()
    plt.plot(dataframe['Date'], dataframe['Unz'], 'teal', label='Vadose water stock')
    plt.ylim(0, max_stocks)
    plt.ylabel('mm')
    plt.legend(loc='upper right', ncol=1, framealpha=1, fancybox=False)
    ax.tick_params(axis='x', which='major', labelsize=8)
    # 3
    ax = fig.add_subplot(gs[4, col2:])
    plt.grid(grid)
    plt.plot(dataframe['Date'], dataframe['Cpy'], 'limegreen', label='Canopy water stock')
    plt.plot(dataframe['Date'], dataframe['Sfs'], 'tab:blue', label='Surface water stock')
    plt.ylim(0, max_stocks)
    plt.ylabel('mm')
    plt.legend(loc='upper right', ncol=2, framealpha=1, fancybox=False)
    ax.tick_params(axis='x', which='major', labelsize=8)
    #
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        if suff != '':
            filepath = folder + '/' + filename + '_' + suff + '.png'
        else:
            filepath = folder + '/' + filename + '.png'
        plt.savefig(filepath, dpi=600)
        plt.close(fig)
        plt.clf()
        return filepath


def plot_lulc_view(lulc, lulc_df, basin, meta, mapttl='lulc', filename='mapview', folder='C:/bin', metadata=False, show=False):
    from geo import reclassify, mask
    from matplotlib.colors import ListedColormap
    colors = lulc_df['ColorLULC'].values
    names = lulc_df['LULCName'].values
    ids = lulc_df['IdLULC'].values
    ranges = [np.min(ids), np.max(ids)]
    cmap = ListedColormap(colors)
    #
    fig = plt.figure(figsize=(14, 9))  # Width, Height
    gs = mpl.gridspec.GridSpec(6, 10, wspace=0.5, hspace=0.5)
    #
    ax = fig.add_subplot(gs[:4, :4])
    fmap = mask(lulc, basin)
    im = plt.imshow(fmap, cmap=cmap, vmin=ranges[0], vmax=ranges[1])
    plt.title(mapttl)
    plt.axis('off')
    #
    #
    # canopy
    fmap = reclassify(lulc, upvalues=ids, classes=lulc_df['f_Canopy'].values)
    fmap = mask(fmap, basin)
    ax = fig.add_subplot(gs[:2, 4:6])
    im = plt.imshow(fmap, cmap='viridis_r')
    plt.title('Canopy factor')
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # Surface
    fmap = reclassify(lulc, upvalues=ids, classes=lulc_df['f_Surface'].values)
    fmap = mask(fmap, basin)
    ax = fig.add_subplot(gs[:2, 6:8])
    im = plt.imshow(fmap, cmap='viridis_r', vmin=0)
    plt.title('Surface factor')
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # RD
    fmap = reclassify(lulc, upvalues=ids, classes=lulc_df['f_RootDepth'].values)
    fmap = mask(fmap, basin)
    ax = fig.add_subplot(gs[:2, 8:10])
    im = plt.imshow(fmap, cmap='viridis_r', vmin=0)
    plt.title('RootDepth factor')
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # RD
    fmap = reclassify(lulc, upvalues=ids, classes=lulc_df['f_IRA'].values)
    fmap = mask(fmap, basin)
    ax = fig.add_subplot(gs[2:4, 6:8])
    im = plt.imshow(fmap, cmap='YlGnBu', vmin=0)
    plt.title('IRA factor')
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # RD
    fmap = reclassify(lulc, upvalues=ids, classes=lulc_df['f_IRI'].values)
    fmap = mask(fmap, basin)
    ax = fig.add_subplot(gs[2:4, 8:10])
    im = plt.imshow(fmap, cmap='YlGnBu', vmin=0)
    plt.title('IRI factor')
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # RD
    fmap = reclassify(lulc, upvalues=ids, classes=lulc_df['C_USLE'].values)
    fmap = mask(fmap, basin)
    ax = fig.add_subplot(gs[4:, 6:8])
    im = plt.imshow(fmap, cmap='BrBG_r', vmin=0)
    plt.title('USLE C factor')
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # RD
    fmap = reclassify(lulc, upvalues=ids, classes=lulc_df['P_USLE'].values)
    fmap = mask(fmap, basin)
    ax = fig.add_subplot(gs[4:, 8:10])
    im = plt.imshow(fmap, cmap='BrBG_r', vmin=0)
    plt.title('USLE P factor')
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    #
    ax = fig.add_subplot(gs[4:, 1:3])
    labels = lulc_df['LULCName']
    y_pos = np.arange(len(labels))
    areas = lulc_df['f_Canopy']
    ax.barh(y_pos, areas, align='center', color=colors)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('% area')
    ax.set_title('lulc distribution')


    if show:
        plt.show()
        plt.close(fig)
    else:
        expfile = folder + '/' + filename + '.png'
        plt.savefig(expfile)
        plt.close(fig)
        return expfile


def plot_shrumap_view(lulc, soils, meta, shruparam, filename='mapview', folder='C:/bin', ttl='SHRU', metadata=True, show=False):
    from matplotlib.colors import ListedColormap
    cmap_lulc = ListedColormap(shruparam['ColorLULC'].values)
    cmap_soil = ListedColormap(shruparam['ColorSoil'].values)
    ranges_lulc = (np.min(shruparam['IdLULC'].values), np.max(shruparam['IdLULC'].values))
    ranges_soil = (np.min(shruparam['IdSoil'].values), np.max(shruparam['IdSoil'].values))
    #
    fig = plt.figure(figsize=(6, 4.5))  # Width, Height
    gs = mpl.gridspec.GridSpec(3, 4, wspace=0.0, hspace=0.0)
    #
    ax = fig.add_subplot(gs[:, :3])
    im = plt.imshow(lulc, cmap=cmap_lulc, vmin=ranges_lulc[0], vmax=ranges_lulc[1])
    im = plt.imshow(soils, cmap=cmap_soil, vmin=ranges_soil[0], vmax=ranges_soil[1], alpha=0.5)
    plt.title(ttl)
    plt.axis('off')
    #
    # lengend
    ax = fig.add_subplot(gs[:, 3:])
    plt.text(x=0.0, y=1.0, s='LULC x Soils')
    plt.plot([0, 1], [0, 1], '.', alpha=0.0)
    hei = 0.95
    step = 0.2
    wid = len(shruparam['IdSoil'].unique())
    count = 0
    while count < len(shruparam['IdLULC'].values):
        xp = 0.1
        for i in range(wid):
            plt.plot(xp, hei, 's', color=shruparam['ColorLULC'].values[count])
            plt.plot(xp, hei, 's', color=shruparam['ColorSoil'].values[count], alpha=0.5)
            #plt.text(x=xp + 0.05, y=hei - 0.015, s=shruparam['IdSHRU'].values[count])
            xp = xp + step
            count = count + 1
        hei = hei - 0.05
    plt.ylim((0, 1))
    plt.xlim((0, 1.5))
    #
    if metadata:
        plt.text(x=0.0, y=0.3, s='Metadata:')
        plt.text(x=0.0, y=0.25, s='Rows: {}'.format(meta['nrows']))
        plt.text(x=0.0, y=0.2, s='Columns: {}'.format(meta['ncols']))
        plt.text(x=0.0, y=0.15, s='Cell size: {:.1f} m'.format(meta['cellsize']))
        plt.text(x=0.0, y=0.1, s='xll: {:.2f} m'.format(meta['xllcorner']))
        plt.text(x=0.0, y=0.05, s='yll: {:.2f} m'.format(meta['xllcorner']))
    plt.axis('off')
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        expfile = folder + '/' + filename + '.png'
        plt.savefig(expfile)
        plt.close(fig)
        return expfile


def plot_qmap_view(map, meta, colors, names, ranges, mapid='lulc', filename='mapview', folder='C:/bin',
                   metadata=True, show=False):
    """

    Plot generic qualitative map

    :param map: 2d numpy array of map
    :param meta: dictionary of map metadata
    :param colors: iterable of class color names
    :param names: iterable of class names
    :param ranges: tuple of ranges
    :param mapid: string of mapid. Ex: 'lulc' or 'soils'
    :param filename: string filename
    :param folder: string folder path
    :param metadata: boolean to print metadata in figure
    :param show: boolean to show instead of saving
    :return: string filepath
    """
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(colors)
    #
    fig = plt.figure(figsize=(6, 4.5))  # Width, Height
    gs = mpl.gridspec.GridSpec(3, 4, wspace=0.0, hspace=0.0)
    #
    ax = fig.add_subplot(gs[:, :3])
    im = plt.imshow(map, cmap=cmap, vmin=ranges[0], vmax=ranges[1])
    plt.title(mapid)
    plt.axis('off')
    #
    # legend
    ax = fig.add_subplot(gs[:, 3:])
    plt.plot([0, 1], [0, 1], '.', alpha=0.0)
    plt.text(x=0.0, y=1.0, s='Classes')
    hei = 0.95
    for i in range(len(names)):
        plt.plot(0.0, hei, 's', color=colors[i])
        plt.text(x=0.15, y=hei-0.015, s=names[i])
        hei = hei - 0.05
    if metadata:
        plt.text(x=0.0, y=0.3, s='Metadata:')
        plt.text(x=0.0, y=0.25, s='Rows: {}'.format(meta['nrows']))
        plt.text(x=0.0, y=0.2, s='Columns: {}'.format(meta['ncols']))
        plt.text(x=0.0, y=0.15, s='Cell size: {:.1f} m'.format(meta['cellsize']))
        plt.text(x=0.0, y=0.1, s='xll: {:.2f} m'.format(meta['xllcorner']))
        plt.text(x=0.0, y=0.05, s='yll: {:.2f} m'.format(meta['xllcorner']))
    plt.axis('off')
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        expfile = folder + '/' + filename + '.png'
        plt.savefig(expfile)
        plt.close(fig)
        return expfile


def plot_map_view(map, meta, ranges, mapid='dem', mapttl='', filename='mapview', folder='C:/bin',
                  metadata=True, show=False, integration=False, png=True):
    """

    Plot a generic map view

    :param map: 2d numpy array of map
    :param meta: dictionary of map metadata
    :param ranges: tuple of ranges
    :param mapid: string of map id
    :param mapttl: string of map title
    :param filename: string filename
    :param folder: string folder path
    :param metadata: boolean to print metadata on figure
    :param show: boolean to show instead of saving
    :param integration: boolean to show integration units instead of instant units
    :param png: boolean to export as PNG
    :return: string filepath
    """
    from matplotlib import cm
    from matplotlib.colors import ListedColormap
    earth_big = cm.get_cmap('gist_earth_r', 512)
    earthcm = ListedColormap(earth_big(np.linspace(0.10, 0.95, 256)))
    jet_big = cm.get_cmap('jet_r', 512)
    jetcm = ListedColormap(jet_big(np.linspace(0.3, 0.75, 256)))
    viridis_big = cm.get_cmap('viridis_r', 512)
    viridiscm = ListedColormap(viridis_big(np.linspace(0.05, 0.9)))
    map_dct = {'dem': ['BrBG_r', 'Elevation'],
               'slope': ['OrRd', 'Degrees'],
               'twi': ['YlGnBu', 'Index units'],
               'twito': ['YlGnBu', 'Index units'],
               'fto': ['Blues', 'Index units'],
               'etpat': ['Greys_r', 'Index units'],
               'catcha': ['Blues', 'Sq. Meters (log10)'],
               'basin': ['Greys', 'Boolean'],
               'flow':[earthcm, 'mm/d', 'mm'], 
               'flow_v':[jetcm, 'mm/d', 'mm'], 
               'stock':[viridiscm, 'mm', 'mm'],
               'deficit':['jet', 'mm', 'mm'], 
               'VSA':['Blues', 'Boolean', '%'], 
               'RC':['YlOrRd', '%', '%']}
    #
    fig = plt.figure(figsize=(6, 4.5))  # Width, Height
    gs = mpl.gridspec.GridSpec(3, 4, wspace=0.0, hspace=0.0)
    #
    ax = fig.add_subplot(gs[:, :3])
    if mapid == 'catcha':
        map = np.log10(map)
        ranges = np.log10(ranges)
    im = plt.imshow(map, cmap=map_dct[mapid][0], vmin=ranges[0], vmax=ranges[1])
    plt.title(mapttl)
    plt.axis('off')
    plt.colorbar(im, shrink=0.4)
    #
    #
    ax = fig.add_subplot(gs[:, 3:])
    if integration:
        plt.text(x=-0.45, y=0.75, s=map_dct[mapid][2])
    else:
        plt.text(x=-0.45, y=0.75, s=map_dct[mapid][1])
    if metadata:
        plt.text(x=0.0, y=0.3, s='Metadata:')
        plt.text(x=0.0, y=0.25, s='Rows: {}'.format(meta['nrows']))
        plt.text(x=0.0, y=0.2, s='Columns: {}'.format(meta['ncols']))
        plt.text(x=0.0, y=0.15, s='Cell size: {:.1f} m'.format(meta['cellsize']))
        plt.text(x=0.0, y=0.1, s='xll: {:.2f} m'.format(meta['xllcorner']))
        plt.text(x=0.0, y=0.05, s='yll: {:.2f} m'.format(meta['yllcorner']))
    plt.axis('off')
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        filepath = folder + '/' + filename
        if png:
            filepath = filepath + '.png'
        else:
            filepath = filepath + '.jpg'
        plt.savefig(filepath)
        plt.close(fig)
        return filepath


def plot_histograms(countmatrix, xs, ys, xt, yt, show=False, folder='C:/bin', filename='histograms', suff=''):
    """

    Plot histograms of TWI and SHRU

    :param countmatrix: 2d numpy array of count matrix
    :param xs: 1d iterable of x labels of SHRU
    :param ys: 1d iterable of y labels of SHRU
    :param xt: 1d iterable of x labels of TWI
    :param yt: 1d iterable of y labels of TWI
    :param show: boolean to show instead of saving
    :param folder: string to folder
    :param filename: string of filename
    :param suff: string suffix of filename
    :return: string of filepath
    """
    #
    fig = plt.figure(figsize=(12, 16))  # Width, Height
    gs = mpl.gridspec.GridSpec(4, 3, wspace=0.3, hspace=0.3)
    #
    # first histogram
    # twi histogram
    ax = fig.add_subplot(gs[0, :2])
    xt = np.round(xt, 1)
    plt.bar(xt, yt, color='tab:blue')
    plt.ylabel('% Frequency')
    plt.title('TWI Histogram')
    plt.xlabel('TWI values')
    plt.ylim(0, 60)
    ax.tick_params(axis='x', which='major', labelsize=7)
    #
    ax = fig.add_subplot(gs[1, :])
    x = np.arange(0, len(ys))
    plt.bar(x, ys, color='tab:blue')
    plt.xlim((0, len(ys) - 1))
    plt.xlabel('SHRU Ids')
    plt.xticks(x, xs)
    plt.ylabel('% Frequency')
    plt.ylim(0, 60)
    plt.title('SHRU Histogram')
    ax.tick_params(axis='x', which='major', labelsize=7)
    #plt.axis('off')
    #
    # matrix
    ax = fig.add_subplot(gs[2:, :])
    im = plt.imshow(np.log10(countmatrix + 0.01), cmap='viridis', vmin=0)
    y = np.arange(0, len(xt))
    plt.title('Count matrix (2d-Histogram)')
    plt.ylabel('TWI values')
    plt.xlabel('SHRU Ids')
    plt.xticks(x, xs)
    plt.yticks(y, np.round(xt, 1))
    ax.tick_params(axis='both', which='major', labelsize=7)
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        expfile = folder + '/' + filename + '.png'
        plt.savefig(expfile)
        plt.close(fig)
        return expfile


def plot_obssim_zmaps(obs, sim, metric, ranges='local', rangesmetric='local', ttl='title', show=False,
                      filename='obssim_zmaps', folder='C:/bin'):
    fig = plt.figure(figsize=(6, 6),)  # Width, Height
    fig.suptitle('ZMAP | {}'.format(ttl))
    gs = mpl.gridspec.GridSpec(3, 1, wspace=0.3, hspace=0.3)
    if ranges == 'local':
        v_min = np.min(np.array((obs, sim)))
        v_max = np.max(np.array((obs, sim)))
    else:
        v_min = ranges[0]
        v_max = ranges[1]
    if rangesmetric == 'local':
        v_min_m = np.min(metric)
        v_max_m = np.max(metric)
    else:
        v_min_m = rangesmetric[0]
        v_max_m = rangesmetric[1]
    ax = fig.add_subplot(gs[0, 0])
    im = plt.imshow(obs, cmap='Greys_r', vmin=v_min, vmax=v_max)
    plt.title('Observed')
    plt.axis('off')
    ax = fig.add_subplot(gs[1, 0])
    im = plt.imshow(sim, cmap='Greys_r', vmin=v_min, vmax=v_max)
    plt.title('Simulated')
    plt.axis('off')
    ax = fig.add_subplot(gs[2, 0])
    im = plt.imshow(metric, cmap='inferno', vmin=v_min_m, vmax=v_max_m)
    plt.title('Abs Error')
    plt.axis('off')
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        expfile = folder + '/' + filename + '.png'
        plt.savefig(expfile)
        plt.close(fig)
        return expfile


def plot_map_analyst(obs, sim, metric, obs_sig, sim_sig, metric_sig, metrics_dct, ranges='local', metricranges='local',
                     ttl='title', filename='map_analyst', folder='C:/bin', show=False):
    """

    Plot a MAP analyst

    :param obs: 2d numpy array of OBS map
    :param sim: 2d numpy array of SIM map
    :param metric: 2d numpy array of evaluation metric
    :param obs_sig: 1d numpy array of OBS signal
    :param sim_sig: 1d numpy array of SIM signal
    :param metric_sig: 1d numpy array of signal of evaluation metric
    :param metrics_dct: dictonary of global evaluation metrics
    :param ranges: string or tuple of ranges of maps. Default: "local" to use local min max of OBS and SIM
    :param metricranges: string or tuple of ranges of metric map. Default: "local" to use local min max of Metric map
    :param ttl: string of superior title
    :param filename: string of filename
    :param folder: string filepath of export folder
    :param show: boolean to show instead of saving. Default: False
    :return: string of filepath
    """
    fig = plt.figure(figsize=(14, 7), )  # Width, Height
    fig.suptitle(ttl)
    gs = mpl.gridspec.GridSpec(6, 13, wspace=0.3, hspace=0.45)
    #
    x_sig = np.arange(0, len(obs_sig))
    #
    # ranges selector
    if ranges != 'local':
        vmin = ranges[0]
        vmax = ranges[1]
    else:
        vmin = np.min((obs, sim))
        vmax = np.max((obs, sim))
    if metricranges != 'local':
        metric_vmin = metricranges[0]
        metric_vmax = metricranges[1]
    else:
        metric_vmin = np.min(metric)
        metric_vmax = np.max(metric)
    #
    #
    ax = fig.add_subplot(gs[0:3, 0:3])
    im = plt.imshow(obs, cmap='Greys', vmin=vmin, vmax=vmax)
    plt.title('Observed')
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    ax = fig.add_subplot(gs[0:3, 3:6])
    im = plt.imshow(sim, cmap='Greys', vmin=vmin, vmax=vmax)
    plt.title('Simulated')
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    ax = fig.add_subplot(gs[0:3, 7:10])
    im = plt.imshow(metric, cmap='jet', vmin=metric_vmin, vmax=metric_vmax)
    plt.title('Local Error')
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    ax = fig.add_subplot(gs[3:5, 0:10])
    plt.plot(x_sig, obs_sig, label='Observed', c='tab:orange')
    plt.plot(x_sig, sim_sig, label='Simulated', c='tab:blue', alpha=0.5)
    plt.title('Map signal', loc='left')
    plt.legend(loc='upper right', ncol=3)
    plt.xlim((np.min(x_sig), np.max(x_sig)))
    plt.ylim((vmin, 1.2 * vmax))
    plt.xticks([])
    plt.ylabel('Map units')
    #
    ax = fig.add_subplot(gs[5:6, 0:10])
    plt.plot(x_sig, metric_sig, 'tab:red')
    plt.xlim((np.min(x_sig), np.max(x_sig)))
    plt.ylim(metric_vmin, metric_vmax)
    plt.xlabel('Cell ID')
    plt.ylabel('Error')
    #
    ax = fig.add_subplot(gs[3:5, 11:])
    plt.scatter(obs_sig, sim_sig, c='tab:grey', s=15, alpha=0.1, edgecolors='none')
    plt.plot([0, vmax], [0, vmax], 'tab:grey', linestyle='--', label='1:1')
    plt.ylim((vmin, vmax))
    plt.xlim((vmin, vmax))
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.ylabel('Signal Sim')
    plt.xlabel('Signal Obs')
    #
    #
    # metrics
    ax = fig.add_subplot(gs[0:3, 10:])
    x_offset = 0.36
    plt.text(x_offset, 1, s='Map Global Metrics')
    plt.text(x_offset, 0.9, s='Error: {:.2f}'.format(metrics_dct['Error']))
    plt.text(x_offset, 0.84, s='Sq. Error: {:.2f}'.format(metrics_dct['SqErr']))
    plt.text(x_offset, 0.78, s='RMSE: {:.2f}'.format(metrics_dct['RMSE']))
    plt.text(x_offset, 0.5, s='Signal Global Metrics')
    plt.text(x_offset, 0.4, s='NSE: {:.2f}'.format(metrics_dct['NSE']))
    plt.text(x_offset, 0.34, s='KGE: {:.2f}'.format(metrics_dct['KGE']))
    plt.text(x_offset, 0.28, s='R: {:.2f}'.format(metrics_dct['R']))
    plt.axis('off')
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        expfile = folder + '/' + filename + '.png'
        plt.savefig(expfile)
        plt.close(fig)
        return expfile
    
    
def sal_deficit_frame(dgbl, d1, vsa1, d2, vsa2, m1, m2, vmax=100, vmin=0, dgbl_max=100, filename='SAL_d_frame_X',
                      folder='C:/bin', supttl='Sensitivity to the m parameter'):
    fig = plt.figure(figsize=(10, 6), )  # Width, Height
    fig.suptitle(supttl)
    gs = mpl.gridspec.GridSpec(2, 3, wspace=0.3, hspace=0.45)
    #
    #
    ax = fig.add_subplot(gs[0, 0])
    im = plt.imshow(d1, cmap='jet', vmin=vmin, vmax=vmax)
    plt.title('Local Deficit | m = {:.1f}'.format(m1), fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    ax = fig.add_subplot(gs[1, 0])
    im = plt.imshow(d2, cmap='jet', vmin=vmin, vmax=vmax)
    plt.title('Local Deficit | m = {:.1f}'.format(m2), fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    ax = fig.add_subplot(gs[0, 1])
    im = plt.imshow(vsa1, cmap='Blues', vmin=0, vmax=1)
    plt.title('Saturated Areas | m = {:.1f}'.format(m1), fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    ax = fig.add_subplot(gs[1, 1])
    im = plt.imshow(vsa2, cmap='Blues', vmin=0, vmax=1)
    plt.title('Saturated Areas | m = {:.1f}'.format(m2), fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    ax = fig.add_subplot(gs[0, 2])
    plt.plot(0, dgbl, 'bo', markersize=10)
    plt.vlines(x=0, ymin=0, ymax=dgbl_max, colors='k')
    plt.title('Global Deficit = {:.1f} mm'.format(dgbl), fontsize=10)
    plt.axis('off')
    #
    #plt.show()
    expfile = folder + '/' + filename + '.png'
    plt.savefig(expfile)
    plt.close(fig)


def glue_scattergram(models_df, rng_dct, likelihood='Score', criteria='>', behaviroural=0.5,
                     filename='post_scattergram', folder='C:/bin', show=False):
    """
    Plot the 9 scattergrams of GLUE analysis
    :param models_df: pandas dataframe - models dataframe (behavioural)
    :param rng_dct: dictionary - range dictionary with parameter keys followed by '_rng'.
     Example: key "m_rng" would access the range tuple of m parameter
    :param likelihood: string of likelihood index.
    :param criteria: string of behavioural criteria
    :param behaviroural: float of behavioural threshold
    :param filename: string of filename
    :param folder: string of folder path
    :param show: boolean to show instead of saving
    :return: string of filepath
    """
    fig = plt.figure(figsize=(14, 6), )  # Width, Height
    fig.suptitle('GLUE | Posterior scattergrams of behavioural models'
                 ' | Criteria: {} {} {} | N = {}'.format(likelihood, criteria, behaviroural, len(models_df)))
    gs = mpl.gridspec.GridSpec(2, 5, wspace=0.45, hspace=0.45)
    #
    params = ('m', 'qo', 'cpmax', 'sfmax', 'erz', 'ksat', 'c', 'k', 'n')
    units = ('mm', 'mm/d', 'mm', 'mm', 'mm', 'mm/d', '°C', 'days', 'stores units')
    #
    criteria_line = (models_df['m'].values * 0.0) + (behaviroural * 0.97)
    #
    ind = 0
    lcl_prm = params[ind]
    lcl_units = units[ind]
    ax = fig.add_subplot(gs[0, 0])
    plt.title('{}'.format(lcl_prm))
    plt.plot(models_df[lcl_prm].values, models_df[likelihood].values, 'k.')
    plt.plot(models_df[lcl_prm].values, criteria_line, 'tab:red')
    plt.ylabel('L[M|y]')
    plt.xlabel('{}'.format(lcl_units))
    plt.xlim(rng_dct['{}_rng'.format(lcl_prm)])
    plt.ylim((0, 1.1))
    #
    ind = 1
    lcl_prm = params[ind]
    lcl_units = units[ind]
    ax = fig.add_subplot(gs[0, 1])
    plt.title('{}'.format(lcl_prm))
    plt.plot(models_df[lcl_prm].values, models_df[likelihood].values, 'k.')
    plt.plot(models_df[lcl_prm].values, criteria_line, 'tab:red')
    plt.ylabel('L[M|y]')
    plt.xlabel('{}'.format(lcl_units))
    plt.xlim(rng_dct['{}_rng'.format(lcl_prm)])
    plt.ylim((0, 1.1))
    #
    ind = 2
    lcl_prm = params[ind]
    lcl_units = units[ind]
    ax = fig.add_subplot(gs[0, 2])
    plt.title('{}'.format(lcl_prm))
    plt.plot(models_df[lcl_prm].values, models_df[likelihood].values, 'k.')
    plt.plot(models_df[lcl_prm].values, criteria_line, 'tab:red')
    plt.ylabel('L[M|y]')
    plt.xlabel('{}'.format(lcl_units))
    plt.xlim(rng_dct['{}_rng'.format(lcl_prm)])
    plt.ylim((0, 1.1))
    #
    ind = 3
    lcl_prm = params[ind]
    lcl_units = units[ind]
    ax = fig.add_subplot(gs[0, 3])
    plt.title('{}'.format(lcl_prm))
    plt.plot(models_df[lcl_prm].values, models_df[likelihood].values, 'k.')
    plt.plot(models_df[lcl_prm].values, criteria_line, 'tab:red')
    plt.ylabel('L[M|y]')
    plt.xlabel('{}'.format(lcl_units))
    plt.xlim(rng_dct['{}_rng'.format(lcl_prm)])
    plt.ylim((0, 1.1))
    #
    ind = 4
    lcl_prm = params[ind]
    lcl_units = units[ind]
    ax = fig.add_subplot(gs[0, 4])
    plt.title('{}'.format(lcl_prm))
    plt.plot(models_df[lcl_prm].values, models_df[likelihood].values, 'k.')
    plt.plot(models_df[lcl_prm].values, criteria_line, 'tab:red')
    plt.ylabel('L[M|y]')
    plt.xlabel('{}'.format(lcl_units))
    plt.xlim(rng_dct['{}_rng'.format(lcl_prm)])
    plt.ylim((0, 1.1))
    #
    ind = 5
    lcl_prm = params[ind]
    lcl_units = units[ind]
    ax = fig.add_subplot(gs[1, 0])
    plt.title('{}'.format(lcl_prm))
    plt.plot(models_df[lcl_prm].values, models_df[likelihood].values, 'k.')
    plt.plot(models_df[lcl_prm].values, criteria_line, 'tab:red')
    plt.ylabel('L[M|y]')
    plt.xlabel('{}'.format(lcl_units))
    plt.xlim(rng_dct['{}_rng'.format(lcl_prm)])
    plt.ylim((0, 1.1))
    #
    ind = 6
    lcl_prm = params[ind]
    lcl_units = units[ind]
    ax = fig.add_subplot(gs[1, 1])
    plt.title('{}'.format(lcl_prm))
    plt.plot(models_df[lcl_prm].values, models_df[likelihood].values, 'k.')
    plt.plot(models_df[lcl_prm].values, criteria_line, 'tab:red')
    plt.ylabel('L[M|y]')
    plt.xlabel('{}'.format(lcl_units))
    plt.xlim(rng_dct['{}_rng'.format(lcl_prm)])
    plt.ylim((0, 1.1))
    #
    ind = 7
    lcl_prm = params[ind]
    lcl_units = units[ind]
    ax = fig.add_subplot(gs[1, 2])
    plt.title('{}'.format(lcl_prm))
    plt.plot(models_df[lcl_prm].values, models_df[likelihood].values, 'k.')
    plt.plot(models_df[lcl_prm].values, criteria_line, 'tab:red')
    plt.ylabel('L[M|y]')
    plt.xlabel('{}'.format(lcl_units))
    plt.xlim(rng_dct['{}_rng'.format(lcl_prm)])
    plt.ylim((0, 1.1))
    #
    ind = 8
    lcl_prm = params[ind]
    lcl_units = units[ind]
    ax = fig.add_subplot(gs[1, 3])
    plt.title('{}'.format(lcl_prm))
    plt.plot(models_df[lcl_prm].values, models_df[likelihood].values, 'k.')
    plt.plot(models_df[lcl_prm].values, criteria_line, 'tab:red')
    plt.ylabel('L[M|y]')
    plt.xlabel('{}'.format(lcl_units))
    plt.xlim(rng_dct['{}_rng'.format(lcl_prm)])
    plt.ylim((0, 1.1))
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        expfile = folder + '/' + filename + '.png'
        plt.savefig(expfile)
        plt.close(fig)
        return expfile


def glue_ensemble(sim_df, ensemble_df, grid=False, show=False, baseflow=False, scale='log', suff='', filename='glue_ensemble', folder='C:/bin',):
    #
    fig = plt.figure(figsize=(16, 8))  # Width, Height
    fig.suptitle('GLUE | 90% confidence ensemble of behavioural models')
    gs = mpl.gridspec.GridSpec(2, 1, wspace=0.8, hspace=0.6)
    # plot prec
    ax1 = fig.add_subplot(gs[0, 0])
    plt.title('Observed precipitation', loc='left')
    plt.ylabel('mm/d')
    plt.plot(sim_df['Date'], sim_df['Prec'])
    plt.ylim(0, 1.1 * np.max(sim_df['Prec'].values))
    plt.grid(grid)
    # plt.xticks(locs, labels)
    # plot q
    ax2 = fig.add_subplot(gs[1, 0], sharex=ax1)
    plt.title('Simulated flow', loc='left')
    plt.ylabel('mm/d')
    if baseflow:
        label = '90% confidence ensemble (baseflow)'
    else:
        label = '90% confidence ensemble'
    plt.fill_between(x=ensemble_df['Date'], y1=ensemble_df['Lo_90'], y2=ensemble_df['Hi_90'],
                     color='lightsteelblue', label=label)
    plt.plot(ensemble_df['Date'], sim_df['Qobs'], color='tab:grey', label='Observed data')
    if baseflow:
        flow = sim_df['Qb']
        label = 'Maximum Likelihood Model (baseflow)'
    else:
        flow = sim_df['Q']
        label = 'Maximum Likelihood Model'
    plt.plot(ensemble_df['Date'], flow, linestyle='dashed', color='tab:blue', label=label)
    plt.grid(grid)
    if scale == 'log':
        plt.yscale(scale)
    else:
        plt.yscale('linear')
    plt.legend()
    # plt.xticks(locs, labels)
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        if suff == '':
            filepath = folder + '/' + filename + '.png'
        else:
            filepath = folder + '/' + filename + '_' + suff + '.png'

        plt.savefig(filepath)
        plt.close(fig)
        return filepath


def map_series(map_series1, map_series2, rng1, rng2, dates, ttl='Map Series', ttl_s1='Series 1', ttl_s2='Series 2',
               filename='map_series', folder='C:/bin', show=False):
    from matplotlib import cm
    from matplotlib.colors import ListedColormap
    jet_big = cm.get_cmap('jet_r', 512)
    jetcm = ListedColormap(jet_big(np.linspace(0.3, 0.75, 256)))

    fig = plt.figure(figsize=(16, 8), )  # Width, Height
    fig.suptitle(ttl)
    gs = mpl.gridspec.GridSpec(8, 21, wspace=0.5, hspace=0.3)
    #
    # plot series 1
    vmin = rng1[0]
    vmax = rng1[1]
    for i in range(len(map_series1)):
        lcl_x = i * 3
        ax = fig.add_subplot(gs[0:4, lcl_x:lcl_x + 3])
        vmin = np.percentile(map_series1[i], 5)
        vmax = np.percentile(map_series1[i], 95)
        im = plt.imshow(map_series1[i], cmap='hot_r', vmin=np.min(map_series1[i]), vmax=np.max(map_series1[i]))
        plt.title('{} | {}'.format(ttl_s1, dates[i]), fontsize=10)
        plt.colorbar(im, shrink=0.4)
        plt.axis('off')
    #
    # plot series 2
    vmin = rng2[0]
    vmax = rng2[1]
    for i in range(len(map_series2)):
        lcl_x = i * 3
        ax = fig.add_subplot(gs[4:, lcl_x:lcl_x + 3])
        #vmin = np.percentile(map_series2[i], 5)
        #vmax = np.percentile(map_series2[i], 95)
        im = plt.imshow(map_series2[i], cmap=jetcm, vmin=vmin, vmax=vmax)
        plt.title('{} | {}'.format(ttl_s2, dates[i]), fontsize=10)
        plt.colorbar(im, shrink=0.4)
        plt.axis('off')
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        expfile = folder + '/' + filename + '.png'
        plt.savefig(expfile)
        plt.close(fig)
        return expfile


def map_compare(obs, sim, err, obs_z, sim_z, err_z, obs_sg, sim_sg, err_sg, ttl='Date',
                filename='map_compare', folder='C:/bin', show=False):
    fig = plt.figure(figsize=(12, 10), )  # Width, Height
    fig.suptitle(ttl)
    gs = mpl.gridspec.GridSpec(10, 12, wspace=0.2, hspace=0.2)
    #
    ax = fig.add_subplot(gs[0:4, 0:3])
    im = plt.imshow(obs, cmap='Greys', vmin=0, vmax=1)
    plt.title('Observado', fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    ax = fig.add_subplot(gs[0:4, 4:7])
    im = plt.imshow(sim, cmap='Greys', vmin=0, vmax=1)
    plt.title('Simulado', fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    ax = fig.add_subplot(gs[0:4, 9:])
    im = plt.imshow(err, cmap='seismic', vmin=-1.5, vmax=1.5)
    plt.title('Erro local', fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    #
    ax = fig.add_subplot(gs[5:7, 0:3])
    im = plt.imshow(obs_z, cmap='Greys', vmin=0, vmax=1)
    plt.title('Obs. compactado', fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    ax = fig.add_subplot(gs[5:7, 4:7])
    im = plt.imshow(sim_z, cmap='Greys', vmin=0, vmax=1)
    plt.title('Sim. compactado', fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    ax = fig.add_subplot(gs[5:7, 9:])
    im = plt.imshow(err_z, cmap='seismic', vmin=-1.5, vmax=1.5)
    plt.title('Erro local', fontsize=10)
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    #
    lcl_x = np.arange(len(obs_sg))
    ax = fig.add_subplot(gs[8:, 0:3])
    plt.plot(lcl_x, obs_sg, 'tab:blue')
    plt.title('Sinal observado', fontsize=10)
    plt.ylim((0, 1))
    plt.xlabel('id')
    #
    ax = fig.add_subplot(gs[8:, 4:7])
    plt.plot(lcl_x, sim_sg, 'tab:orange')
    plt.title('Sinal simulado', fontsize=10)
    plt.ylim((0, 1))
    plt.xlabel('id')
    #
    ax = fig.add_subplot(gs[8:, 9:])
    plt.plot(lcl_x, err_sg, 'tab:red')
    plt.title('Erro local', fontsize=10)
    plt.ylim((-1.5, 1.5))
    plt.xlabel('id')
    #
    if show:
        plt.show()
        plt.close(fig)
    else:
        expfile = folder + '/' + filename + '.png'
        plt.savefig(expfile)
        plt.close(fig)
        return expfile


def plot_lulc_view(lulc, lulcparam_df, areas_df, aoi, meta, mapttl='lulc', filename='mapview', folder='C:/bin',
                   metadata=False, show=False):
    """
    Plot LULC view analyst
    :param lulc: 2d numpy array of LULC classes
    :param lulcparam_df: pandas dataframe object of lulc parameters
    :param areas_df: pandas dataframe object of areas
    :param aoi: 2d numpy array of AOI
    :param meta: metadata dictionary for maps
    :param mapttl: string title
    :param filename: string filename
    :param folder: string path to output directory
    :param metadata: boolean to plot metadata
    :param show: boolean to show instead of saving
    :return: none
    """
    from geo import reclassify, mask
    from matplotlib.colors import ListedColormap
    colors = lulcparam_df['ColorLULC'].values
    names = lulcparam_df['LULCName'].values
    ids = lulcparam_df['IdLULC'].values
    ranges = [np.min(ids), np.max(ids)]
    cmap = ListedColormap(colors)
    #
    fig = plt.figure(figsize=(14, 9))  # Width, Height
    gs = mpl.gridspec.GridSpec(8, 13, wspace=0.5, hspace=0.5)
    #
    ax = fig.add_subplot(gs[:4, :4])
    fmap = mask(lulc, aoi)
    im = plt.imshow(fmap, cmap=cmap, vmin=ranges[0], vmax=ranges[1])
    plt.title(mapttl)
    plt.axis('off')
    #
    #
    # canopy map
    fmap = reclassify(lulc, upvalues=ids, classes=lulcparam_df['f_Canopy'].values)
    fmap = mask(fmap, aoi)
    ax = fig.add_subplot(gs[4:6, 0:2])
    im = plt.imshow(fmap, cmap='viridis_r')
    plt.title('Canopy factor', fontdict={'fontsize': 10})
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # Surface
    fmap = reclassify(lulc, upvalues=ids, classes=lulcparam_df['f_Surface'].values)
    fmap = mask(fmap, aoi)
    ax = fig.add_subplot(gs[4:6, 2:4])
    im = plt.imshow(fmap, cmap='viridis_r', vmin=0)
    plt.title('Surface factor', fontdict={'fontsize': 10})
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # RD
    fmap = reclassify(lulc, upvalues=ids, classes=lulcparam_df['f_RootDepth'].values)
    fmap = mask(fmap, aoi)
    ax = fig.add_subplot(gs[4:6, 4:6])
    im = plt.imshow(fmap, cmap='viridis_r', vmin=0)
    plt.title('RootDepth factor', fontdict={'fontsize': 10})
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # IRA
    fmap = reclassify(lulc, upvalues=ids, classes=lulcparam_df['f_IRA'].values)
    fmap = mask(fmap, aoi)
    ax = fig.add_subplot(gs[6:, 0:2])
    im = plt.imshow(fmap, cmap='YlGnBu', vmin=0)
    plt.title('IRA factor', fontdict={'fontsize': 10})
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # IRI
    fmap = reclassify(lulc, upvalues=ids, classes=lulcparam_df['f_IRI'].values)
    fmap = mask(fmap, aoi)
    ax = fig.add_subplot(gs[6:, 2:4])
    im = plt.imshow(fmap, cmap='YlGnBu', vmin=0)
    plt.title('IRI factor', fontdict={'fontsize': 10})
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # C USLE
    fmap = reclassify(lulc, upvalues=ids, classes=lulcparam_df['C_USLE'].values)
    fmap = mask(fmap, aoi)
    ax = fig.add_subplot(gs[6: , 4:6])
    im = plt.imshow(fmap, cmap='BrBG_r', vmin=0)
    plt.title('USLE C factor', fontdict={'fontsize': 10})
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    # P USLE
    fmap = reclassify(lulc, upvalues=ids, classes=lulcparam_df['P_USLE'].values)
    fmap = mask(fmap, aoi)
    ax = fig.add_subplot(gs[6: , 6:8])
    im = plt.imshow(fmap, cmap='BrBG_r', vmin=0)
    plt.title('USLE P factor', fontdict={'fontsize': 10})
    plt.colorbar(im, shrink=0.4)
    plt.axis('off')
    #
    #
    ax = fig.add_subplot(gs[:3, 5:6])
    labels = lulcparam_df['LULCName']
    y_pos = np.arange(len(labels))
    bars = areas_df['Area_%'].values
    ax.barh(y_pos, bars, align='center', color=colors)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('%')
    ax.set_title('% areas', fontdict={'fontsize': 10})
    #
    ax = fig.add_subplot(gs[:3, 6:7])
    y_pos = np.arange(len(labels))
    bars = lulcparam_df['f_Canopy'].values
    ax.barh(y_pos, bars, align='center', color='tab:grey')
    ax.set_yticks(y_pos)
    ax.set_yticklabels([])
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Factor')
    ax.set_title('f_Canopy', fontdict={'fontsize': 10})
    #
    ax = fig.add_subplot(gs[:3, 7:8])
    y_pos = np.arange(len(labels))
    bars = lulcparam_df['f_Surface'].values
    ax.barh(y_pos, bars, align='center', color='tab:grey')
    ax.set_yticks(y_pos)
    ax.set_yticklabels([])
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Factor')
    ax.set_title('f_Surface', fontdict={'fontsize': 10})
    #
    ax = fig.add_subplot(gs[:3, 8:9])
    y_pos = np.arange(len(labels))
    bars = lulcparam_df['f_RootDepth'].values
    ax.barh(y_pos, bars, align='center', color='tab:grey')
    ax.set_yticks(y_pos)
    ax.set_yticklabels([])
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Factor')
    ax.set_title('f_RootDepth', fontdict={'fontsize': 10})
    #
    ax = fig.add_subplot(gs[:3, 9:10])
    y_pos = np.arange(len(labels))
    bars = lulcparam_df['f_IRA'].values
    ax.barh(y_pos, bars, align='center', color='tab:grey')
    ax.set_yticks(y_pos)
    ax.set_yticklabels([])
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Factor')
    ax.set_title('f_IRA', fontdict={'fontsize': 10})
    #
    ax = fig.add_subplot(gs[:3, 10:11])
    y_pos = np.arange(len(labels))
    bars = lulcparam_df['f_IRA'].values
    ax.barh(y_pos, bars, align='center', color='tab:grey')
    ax.set_yticks(y_pos)
    ax.set_yticklabels([])
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Factor')
    ax.set_title('f_IRA', fontdict={'fontsize': 10})
    #
    ax = fig.add_subplot(gs[:3, 11:12])
    y_pos = np.arange(len(labels))
    bars = lulcparam_df['C_USLE'].values
    ax.barh(y_pos, bars, align='center', color='tab:grey')
    ax.set_yticks(y_pos)
    ax.set_yticklabels([])
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Factor')
    ax.set_title('C_USLE', fontdict={'fontsize': 10})
    #
    ax = fig.add_subplot(gs[:3, 12:13])
    y_pos = np.arange(len(labels))
    bars = lulcparam_df['P_USLE'].values
    ax.barh(y_pos, bars, align='center', color='tab:grey')
    ax.set_yticks(y_pos)
    ax.set_yticklabels([])
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Factor')
    ax.set_title('P_USLE', fontdict={'fontsize': 10})

    if show:
        plt.show()
        plt.close(fig)
    else:
        expfile = folder + '/' + filename + '.png'
        plt.savefig(expfile)
        plt.close(fig)
        return expfile

