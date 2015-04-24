# ------- #
# Normal Mixture #
# ------- #
# Normal Distribution Functions 
def norm_means(data): 
    cols = data.shape[1]
    return np.repeat(0.0,cols) 

def norm_cov(data):
    m = data.shape[1]
    covs = np.repeat(1.0,m) 
    return np.diag(covs)

def norm_singdist(ng, data):
    m = data.shape[1]
    dist = mixture.MultiNormalDistribution(m, 
        norm_means(data),norm_cov(data))
    return dist

def norm_multdist(ng, data):
    temp = list()
    for x in range(ng):
        temp.append(norm_singdist(2, TO1adj))
    return temp

# Data functions
def build_mix_dat(data):
    mixdat = mixture.DataSet()
    mixdat.fromArray(data)
    return mixdat

# Normal Mixture Model 
def intialize_normal_model(ng, data):
    mod_ps = np.repeat(1.0/ng, ng)
    if ng ==2:
        n1,n2 = norm_multdist(ng, data)
        mix_ = mixture.MixtureModel(ng, mod_ps,[n1,n2])
    elif ng == 3:  
        n1,n2,n3 = norm_multdist(ng, data)
        mix_ = mixture.MixtureModel(ng, mod_ps,[n1,n2,n3])
    elif ng == 4:  
        n1,n2,n3,n4 = norm_multdist(ng, data)
        mix_ = mixture.MixtureModel(ng, mod_ps,[n1,n2,n3,n4])
    elif ng == 5:  
        n1,n2,n3,n4,n5 = norm_multdist(ng, data)
        mix_ = mixture.MixtureModel(ng, mod_ps,[n1,n2,n3,n4,n5])
    elif ng == 6:  
        n1,n2,n3,n4,n5,n6 = norm_multdist(ng, data)
        mix_ = mixture.MixtureModel(ng, mod_ps,[n1,n2,n3,n4,n5,n6])
    elif ng == 7:  
        n1,n2,n3,n4,n5,n6,n7 = norm_multdist(ng, data)
        mix_ = mixture.MixtureModel(ng, mod_ps,[n1,n2,n3,n4,n5,n6,n7])
    elif ng == 8:  
        n1,n2,n3,n4,n5,n6,n7,n8 = norm_multdist(ng, data)
        mix_ = mixture.MixtureModel(ng, mod_ps,[n1,n2,n3,n4,n5,n6,n7,n8])
    return mix_ 

def normal_mixmod(ng, data):
    mix_mod = intialize_normal_model(ng, data)
    mix_dat = build_mix_dat(data)
    mix_mod.modelInitialization(mix_dat)
    mix_mod.EM(mix_dat, 40,.2)
    mix_mod.classify(mix_dat)
    return mix_mod
   
# Results 
def normal_results(ng,data): 
    out = normal_mixmod(ng, data)
    traj = list()
    for i in range(ng):
        traj.append(out.components[i].distList[0].mu)
    return traj
