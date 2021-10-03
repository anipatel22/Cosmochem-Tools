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
