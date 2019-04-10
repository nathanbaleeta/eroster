import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";

import Header from "../Layout/Header";
import Navigation from "../Layout/Navigation";

const styles = {};

function Dashboard(props) {
  //const { classes } = props;
  return (
    <div>
      <Header />
      <Navigation />
    </div>
  );
}

Dashboard.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(Dashboard);
