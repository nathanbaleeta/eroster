import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import { Switch, Route } from "react-router-dom";

import TabNavigation from "./TabNavigation";

import AgencyFilter from "../Agency/AgencyFilter";
import AgencyList from "../Agency/AgencyList";
import ConsultantList from "../Consultant/ConsultantList";

const styles = theme => ({
  main: {
    padding: 3 * theme.spacing.unit,
    [theme.breakpoints.down("xs")]: {
      padding: 2 * theme.spacing.unit
    }
  },

  link: {
    textDecoration: "none",
    color: "white"
  }
});

function Navigation(props) {
  const { classes } = props;

  return (
    <div className={classes.root}>
      <TabNavigation />
      <br />
      <br />
      <main className={classes.main}>
        <Grid container spacing={24}>
          <Grid item xs={3} sm={3}>
            <br />
            <br />

            <AgencyFilter />
          </Grid>
          <Grid item xs={9} sm={9}>
            <Switch>
              <Route path="/agency/agencies" component={AgencyList} />
              <Route path="/agency/consultants" component={ConsultantList} />
            </Switch>
          </Grid>
        </Grid>
      </main>
    </div>
  );
}

Navigation.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(Navigation);
