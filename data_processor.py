# This function takes a standardized isotope ratio list as an input and converts it to mass fraction ration. The standards and scale (delta, epsilon, or mu) must also be inputted as a list and string respectively.
def to_mfrac_ratio(ratio, std, scale):
        mfrac_ratio = []
        if scale == 'delta':
            for i in range(len(ratio)):
                mfrac_ratio.append((ratio[i]/1000 + 1) * std[i])
        elif scale == 'epsilon':
            for i in range(len(ratio)):
                mfrac_ratio.append((ratio[i]/10000 + 1) * std[i])
        elif scale == 'mu':
            for i in range(len(ratio)):
                mfrac_ratio.append((ratio[i]/1000000 + 1) * std[i])
        return mfrac_ratio

# This function does the opposite of the above function. Taking mass fraction ratio list as input and converting to a standardized isotope ratio list scaled to either delta, epsilon, or mu.
def to_scaled_ratio(mfrac, std, scale):
        ratio = []
        if scale == 'delta':
            for i in range(len(mfrac)):
                ratio.append((mfrac[i]/std[i]-1) * 1000)
        elif scale == 'epsilon':
            for i in range(len(mfrac)):
                ratio.append((mfrac[i]/std[i]-1) * 10000)
        elif scale == 'mu':
            for i in range(len(mfrac)):
                ratio.append((mfrac[i]/std[i]-1) * 1000000)
        return ratio

# This function takes a mass fraction ratio list and gets the absolute mass fractions (within the sample) for each isotope.
def get_mfrac(mfrac_ratio):
        mfrac = []
        tot = sum(mfrac_ratio)
        for i in range(len(mfrac_ratio)):
            mfrac.append(mfrac_ratio[i]/tot)
        return mfrac

# This function takes an absolute mass fraction list and reference isotope (the desired denominator in the mass fraction ratios) and outputs a mass fraction ratio list.
def get_mfrac_ratio(mfrac, ref_iso):
        mfrac_ratio = []
        for i in range(len(mfrac)):
            mfrac_ratio.append(mfrac[i]/ref_iso)
        return mfrac_ratio


