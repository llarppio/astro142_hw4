#
# (c) 2023 Michael Fitzgerald (mpfitz@ucla.edu)
#
# Some code for querying Simbad for making a target list.
#


from astroquery.simbad import Simbad

import logging
_log = logging.getLogger('hw4prob1')



def format_target_list(target_list):
    """Query Simbad for list of identifiers; returns dictionary with RA and Dec strings"""

    # an empty dictionary to hold our output
    target_info = {}
    
    # get the Simbad query for M45 (the Pleiades)
    for target_name in target_list:
        _log.debug('querying {}'.format(target_name))
        result_table = Simbad.query_object(target_name)

        # report on results
        n_result = len(result_table)
        _log.info('{}: {} objects found'.format(target_name, n_result))
        if n_result == 0:
            _log.warn('skipping....')
            continue
        if n_result > 1:
            _log.warn('using first result')

        # store RA and DEC strings as tuple for this object
        ra = result_table['RA'][0]
        dec = result_table['DEC'][0]
        target_info[target_name] = (ra, dec)

    # sort dictionary by the "value" (ra,dec)
    target_info = dict(sorted(target_info.items(), key=lambda x:x[1]))

    return target_info


if __name__ == '__main__':

    # set up logging output
    #logging.basicConfig(level=logging.INFO,
    logging.basicConfig(level=logging.DEBUG,
                        format='%(name)-12s: %(levelname)-8s %(message)s',
                        )

    # define target list
    target_list = ['M2',
                   'M45',
                   'HD 189733',
                   '3C 273',
                   'NGC 1068',
                   'AU Mic',
                   'TRAPPIST-1'
                   ]

    target_info = format_target_list(target_list)

    # output results to nicely formatted file
    output_fn = 'target_list.txt'
    with open(output_fn, 'w') as f:
        for tn, (ra, dec) in target_info.items():
            # print the output to file
            #   See https://docs.python.org/3/tutorial/inputoutput.html for string
            #   formatting for the fixed-width output
            print(f'{tn:20} {ra:20} {dec:20}', file=f)

