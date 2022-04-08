def to_iso_ratio(ratio, standard, scale = 'delta'):
    # this function converts isotopic data in delta, epsiolon, or mu notation to isotopic ratios
        iso_ratio = []
        scales = {'delta':1000, 'epsilon': 10000, 'mu':1000000}
        for i in range(len(ratio)):
            iso_ratio.append((ratio[i]/scales[scale] + 1) * standard[i])
        return iso_ratio

def to_scaled_ratio(iso_ratio, standard, scale = 'delta'):
    # this function converts isotopic ratios into delta, epsilon, or my notation
        scaled_ratio = []
        scales = {'delta':1000, 'epsilon': 10000, 'mu':1000000}
        for i in range(len(iso_ratio)):
            scaled_ratio.append((iso_ratio[i]/standard[i]-1) * scales[scale])
        return scaled_ratio

def get_mfrac(iso_ratio):
    # this function gets mass fractions from isotopic ratios
        mfrac = []
        tot = sum(iso_ratio)
        for i in range(len(iso_ratio)):
            mfrac.append(iso_ratio[i]/tot)
        return mfrac

def get_iso_ratio(mfrac, normalization_isotope):
    # this function gets isotopic ratios from mass fractions and a specified normalization mass fraction
        mfrac_ratio = []
        for i in range(len(mfrac)):
            mfrac_ratio.append(mfrac[i]/normalization_isotope)
        return mfrac_ratio

def mix_mfrac(N1, N2, F):
    # This function performs a mixing calculation between two materials, N1 and N2, as specified by the mixing factor F.
        N_calc = []
        for i in range(len(N1)):
            N_calc.append(N1[i] + F * (N2[i] - N1[i]))
        return N_calc

#Functions for Error Propagation

def get_mfrac_var(iso_ratio, var_iso_ratio):
    # This function takes three lists as inputs: isotopic ratio of each species, 
    # the variance for each ratio, and the covariance between each ratio and the sum of the ratios.
    # It returns a list containing the variances (sd squared) of the mass fraction for each species.
        var_d = 0
        d = 0
        var_mfrac = []
        for i in range(len(iso_ratio)):
            d += iso_ratio[i]
            var_d += var_iso_ratio[i]
        for i in range(len(iso_ratio)):
            var_mfrac.append((iso_ratio[i]/d)**2 * (var_iso_ratio[i]/(iso_ratio[i])**2 + var_d/(d**2)))
        return var_mfrac

# - 2*iso_ratio_cov[i]/(d*iso_ratio[i])
def get_iso_ratio_var(mfrac, var_mfrac, norm):
    # This function takes two list (mass fraction and variance of mass fraction) 
    # and an int (index of normaliozation isotope) as inputs. The output is a list of variance of the isotopic ratios.
        var_iso_ratio = []
        for i in range(len(mfrac)):
            var_iso_ratio.append((mfrac[i]/mfrac[norm])**2 * (var_mfrac[i]/mfrac[i]**2 + var_mfrac[norm]/mfrac[norm]**2))
        return var_iso_ratio
        
def to_scaled_ratio_var(iso_ratio, var_iso_ratio, standard, var_standard, scale = 'delta'):
    # This function takes 4 lists as inputs: isotopic ratio and correposning variances. Standard ratios and corresponding variances.
    # One can also specify the scale (i.e delta, epsilon, or mu - see "to_scaled_ratio" function above).
    # The output is a list containing variances of scaled ratio values.
        scales = {'delta':1000, 'epsilon': 10000, 'mu':1000000}
        var_scaled_ratio = []
        for i in range(len(iso_ratio)):
            var_scaled_ratio.append(scales[scale]**2 * (iso_ratio[i]/standard[i])**2 * (var_iso_ratio[i]/iso_ratio[i]**2 + var_standard[i]/standard[i]**2))
        return var_scaled_ratio

def to_iso_ratio_var(scaled_ratio, var_scaled_ratio, standard, var_standard, scale = 'delta'):
    # This function takes 4 lists as inputs: the scaled isotopic ratios (delta, epsilon, or mu) and the correpsoding variances, standard isotopic ratios
    # and correpsonding variances. One can also specify the scale (i.e delta, epsilon, or mu - see "to_scaled_ratio" function above).
    # The output is a list containing variances of isotopic ratios.
        scales = {'delta':1000, 'epsilon': 10000, 'mu':1000000}
        var_iso_ratio = []
        for i in range(len(scaled_ratio)):
            if (scaled_ratio[i] != 0.0 and standard[i] != 0.0):
                var_iso_ratio.append(var_standard[i] + ((scaled_ratio[i] * standard[i]/scales[scale])**2) * (var_scaled_ratio[i]/(scaled_ratio[i])**2 + var_standard[i]/(standard[i]**2)))
            else:    
                var_iso_ratio.append(var_standard[i])
        return var_iso_ratio