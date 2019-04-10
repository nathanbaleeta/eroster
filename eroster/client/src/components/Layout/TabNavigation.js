import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Tab from "@material-ui/core/Tab";
import Tabs from "@material-ui/core/Tabs";
import { Link } from "react-router-dom";

import GroupIcon from "@material-ui/icons/Group";
import PhotoCameraIcon from "@material-ui/icons/PhotoCamera";

const styles = theme => ({
  root: {
    width: "100%"
  },

  link: {
    textDecoration: "none",
    color: "white"
  }
});

function TabNavigation(props) {
  const { classes } = props;

  return (
    <div className={classes.root}>
      <br />
      <br />

      <br />
      <Paper className={classes.root}>
        <Tabs indicatorColor="primary" textColor="secondary">
          <Link to="/agency/agencies" className={classes.link}>
            <Tab
              label="Agencies"
              icon={<GroupIcon />}
              style={{
                color: "black",
                //fontWeight: "bold",
                fontSize: "18px",
                borderRight: "1px solid #d4d4d4"
              }}
            />
          </Link>
          <Link to="/agency/consultants" className={classes.link}>
            <Tab
              label="Consultants"
              icon={<GroupIcon />}
              style={{
                color: "black",
                //fontWeight: "bold",
                fontSize: "18px",
                borderLeft: "1px solid #d4d4d4",
                borderRight: "1px solid #d4d4d4"
              }}
            />
          </Link>

          <Link to="/agency/suppliers" className={classes.link}>
            <Tab
              label="Suppliers"
              icon={<GroupIcon />}
              style={{
                color: "black",
                fontSize: "18px",
                //fontWeight: "bold",
                borderRight: "1px solid #d4d4d4"
              }}
            />
          </Link>

          <Link to="/agency/vendors" className={classes.link}>
            <Tab
              label="Vendors"
              icon={<GroupIcon />}
              style={{
                color: "black",
                fontSize: "18px",
                //fontWeight: "bold",
                borderRight: "1px solid #d4d4d4"
              }}
            />
          </Link>

          <Link to="/agency/working-groups" className={classes.link}>
            <Tab
              label="UN PARTNERS"
              icon={<GroupIcon />}
              style={{
                color: "black",
                fontSize: "18px",
                //fontWeight: "bold",
                borderRight: "1px solid #d4d4d4"
              }}
            />
          </Link>

          <Link to="/agency/working-groups" className={classes.link}>
            <Tab
              label="Working Groups"
              icon={<GroupIcon />}
              style={{
                color: "black",
                fontSize: "18px",
                //fontWeight: "bold",
                borderRight: "1px solid #d4d4d4"
              }}
            />
          </Link>

          <Link to="/agency/reports" className={classes.link}>
            <Tab
              label="Reports"
              icon={<PhotoCameraIcon />}
              style={{
                color: "black",
                fontSize: "18px",
                //fontWeight: "bold",
                borderRight: "1px solid #d4d4d4"
              }}
            />
          </Link>
        </Tabs>
      </Paper>
    </div>
  );
}

TabNavigation.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(TabNavigation);
