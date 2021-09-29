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
        # elif scale == '' and (type(std) == float or type(std) == int):
        #     for i in range(len(ratio)):
        #         mfrac_ratio.append(ratio[i]/std)
        return mfrac_ratio


def to_scaled_ratio(scale, mfrac, std):
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


def get_mfrac(mfrac_ratio):
        mfrac = []
        tot = sum(mfrac_ratio)
        for i in range(len(mfrac_ratio)):
            mfrac.append(mfrac_ratio[i]/tot)
        return mfrac

def get_mfrac_ratio(mfrac, ref_iso):
        mfrac_ratio = []
        for i in range(len(mfrac)):
            mfrac_ratio.append(mfrac[i]/ref_iso)
        return mfrac_ratio


