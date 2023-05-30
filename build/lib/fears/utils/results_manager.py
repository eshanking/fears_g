import os
import pickle
import pandas as pd
from fears_g.utils import dir_manager
# from fears.classes.experiment_class import Experiment

def get_experiment_results(suffix=None,exp=None):
    """
    

    Parameters
    ----------
    data_folder : str
        Name (not path) of the results folder within /fears/results/
    exp_info_file : str
        Name (not path) of the experiment info file (.p) within 
        /fears/results/

    Returns
    -------
    experiment_folders : list
        list of experiment folder paths
    exp_info : Experiment class object
        Experiment class object used to run the experiment

    """
    # exp_info_path = dir_manager.make_resultspath_absolute(exp_info_file)
    # results_dir = dir_manager.make_resultspath_absolute(data_folder)

    if exp is None:
        exp_info_file = 'results_' + suffix + os.sep + 'experiment_info_' + suffix + '.p'
        exp_info_path = dir_manager.make_resultspath_absolute(exp_info_file)

        exp_info = pickle.load(open(exp_info_path,'rb')) # load experiment info
    else:
        exp_info = exp
    
    # experiment_folders = sorted(os.listdir(path=results_dir)) 
    # experiment_folders = [x for x in experiment_folders if x != '.DS_Store']
    # experiment_folders = [results_dir + os.sep + x 
    #                       for x in experiment_folders]
    experiment_folders = exp_info.exp_folders
    return experiment_folders, exp_info

def get_data(sim_path):
    """
    

    Parameters
    ----------
    sim_path : str
        Path of the simulation run to load

    Returns
    -------
    data : numpy array
        Data (typically simulation counts)

    """
    f = open(sim_path,'rb')
    data = pickle.load(f)
    
    return data

def save_fig(fig,savename,bbox_inches='tight'):
    # fig.margins(0,0)
    
    savename = dir_manager.make_figurepath_absolute(savename)
    fig.savefig(savename,bbox_inches=bbox_inches,
                dpi=400,
                transparent=True,
                facecolor='w',
                edgecolor='w')