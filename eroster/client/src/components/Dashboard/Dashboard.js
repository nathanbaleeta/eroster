import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";

import Header from "../Layout/Header";

import Analytics from "./Visualization/Analytics";

const styles = theme => ({
  main: {
    padding: 3 * theme.spacing.unit,
    [theme.breakpoints.down("xs")]: {
      padding: 2 * theme.spacing.unit
    }
  }
});

function Dashboard(props) {
  const { classes } = props;
  return (
    <div>
      <Header />
      <main className={classes.main}>
        <Analytics />
      </main>
    </div>
  );
}

Dashboard.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(Dashboard);
