import argparse

import FundamentalAnalysis as fa  # Financial Modeling Prep

import config_terminal as cfg


# ---------------------------------------------------- RATING ----------------------------------------------------
def rating(l_args, s_ticker):
    parser = argparse.ArgumentParser(prog='rating',
                                     description="""Based on specific ratios, prints information whether the company
                                     is a (strong) buy, neutral or a (strong) sell. The following fields are expected:
                                     P/B, ROA, DCF, P/E, ROE, and D/E. [Source: Financial Modeling Prep]""")

    (ns_parser, l_unknown_args) = parser.parse_known_args(l_args)

    if l_unknown_args:
        print(f"The following args couldn't be interpreted: {l_unknown_args}\n")
        return

    df_fa = fa.rating(s_ticker, cfg.API_KEY_FINANCIALMODELINGPREP)
    print(df_fa)

    print("")
