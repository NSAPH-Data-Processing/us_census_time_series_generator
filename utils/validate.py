def validate_census_variable(cfg):
    variable = cfg.variable
    
    # == validate variables has entries for surveys dec, acs1, and acs5 ==
    surveys = cfg.census.variables[variable].keys()
    if set(surveys) != {'dec', 'acs1', 'acs5'}:
        raise ValueError(f"Variable {variable} does not have all surveys dec, acs1, and acs5")

    # == validate segment years are the same as year coverage for all surveys survey attached to a variable ==
    for survey in cfg.census.variables[variable].keys(): 
        years = cfg.census.variables[variable][survey].year_coverage
        if years is None:
            years = []
        
        segment_years = []
        if cfg.census.variables[variable][survey].segments is not None:
            # concatenate segment years
            for segment in cfg.census.variables[variable][survey].segments:
                segment_years.append(segment.years)
            segment_years = [item for sublist in segment_years for item in sublist]
        # if segment_years is not the same as years, raise an error and stop the program
        
        if set(segment_years) != set(years):
            raise ValueError(f"Years in segments do not match years for variable {variable} and survey {survey}")

def validate_census_yaml(cfg):
    # == validate all variables have surveys dec, acs1, and acs5 ==
    for variable in cfg.census:
        surveys = cfg.census.variables[variable].keys()
        if set(surveys) != {'dec', 'acs1', 'acs5'}:
            raise ValueError(f"Variable {variable} does not have all surveys dec, acs1, and acs5")

    # == validate segment years are the same as year coverage for each variable/survey ==
    for variable in cfg.census.keys():
        for survey in cfg.census.variables[variable].keys(): 
            years = cfg.census.variables[variable][survey].year_coverage
            if years is None:
                years = []
            
            segment_years = []
            if cfg.census.variables[variable][survey].segments is not None:
                # concatenate segment years
                for segment in cfg.census.variables[variable][survey].segments:
                    segment_years.append(segment.years)
                segment_years = [item for sublist in segment_years for item in sublist]
            # if segment_years is not the same as years, raise an error and stop the program
            
            if set(segment_years) != set(years):
                raise ValueError(f"Years in segments do not match years for variable {variable} and survey {survey}")
