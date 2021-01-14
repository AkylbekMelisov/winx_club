def spam(str1):
    if "asap" in str1 or "urgent" in str1 or "help" in str1 or str1.isupper() and str1.endswith('!!!'):
        print('Стивену')
    else:
        print('mne')
spam("ADS  EFSF!!!")