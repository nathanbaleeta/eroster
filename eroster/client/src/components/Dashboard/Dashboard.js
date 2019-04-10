import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";

import Header from "../Layout/Header";

import Analytics from "./Visualization/Analytics";

const styles = {};

function Dashboard(props) {
  //const { classes } = props;
  return (
    <div>
      <Header />
      <Analytics />
    </div>
  );
}

Dashboard.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(Dashboard);
