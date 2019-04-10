import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";

import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import { Link } from "react-router-dom";
import Tooltip from "@material-ui/core/Tooltip";

import Avatar from "@material-ui/core/Avatar";

import JoinHeader from "../Layout/JoinHeader";

const styles = theme => ({
  paper: {
    padding: theme.spacing.unit * 2,
    textAlign: "center",
    color: theme.palette.text.secondary
  },

  gridContainer: {
    marginTop: -20,
    marginLeft: -24,
    marginRight: -70,
    //marginRight: "auto",
    //marginLeft: "auto",
    height: "auto",
    backgroundSize: "100vw 100vh",
    minHeight: "100%",
    minWidth: "100%",
    backgroundRepeat: "no-repeat",
    backgroundImage: `url(${"/static/images/b.jpg"})`,

    zIndex: 1000,
    position: "fixed"
  },

  bigAvatar: {
    margin: 10,
    width: 60,
    height: 60
  }
});

function Join(props) {
  const { classes } = props;

  return (
    <div>
      <JoinHeader />
      <Grid container spacing={24} className={classes.gridContainer}>
        <Grid item xs={6} sm={1} />
        <Grid item xs={6} sm={6}>
          <Grid container spacing={24}>
            <Grid item xs={12} sm={12} style={{ marginTop: 70 }}>
              <Typography variant="h4" style={{ color: "#ffffff" }}>
                Where professionals join the UN family
              </Typography>
              <Typography
                variant="body2"
                gutterBottom
                style={{ fontSize: "17px", color: "#ffffff" }}
              >
                One stop site for professionals to post their resumes and get
                notified when a job profile matches their qualifications.
              </Typography>
            </Grid>
          </Grid>
        </Grid>
        <Grid item xs={6} sm={1} />
        <Grid item xs={6} sm={4}>
          <br />
          <br />
          <Paper className={classes.paper} style={{ marginRight: 80 }}>
            <Grid container justify="center" alignItems="center">
              <Avatar
                alt="Remy Sharp"
                src="/static/images/un.jpg"
                className={classes.bigAvatar}
              />
            </Grid>
            <Typography
              className={classes.title}
              variant="h4"
              //color="inherit"
              noWrap
              style={{ color: "black" }}
            >
              Sign In!
            </Typography>
            <br />

            <Grid item xs={12} sm={12}>
              <TextField
                id="outlined-uncontrolled"
                label="Email"
                className={classes.textField}
                margin="normal"
                variant="outlined"
                fullWidth
              />
            </Grid>
            <Grid item xs={12} sm={12}>
              <TextField
                id="outlined-uncontrolled"
                label="Password"
                type="Password"
                className={classes.textField}
                margin="normal"
                variant="outlined"
                fullWidth
              />
            </Grid>
            <br />
            <br />

            <Link to="/dashboard" className={classes.link}>
              <Tooltip title="Profile">
                <Button
                  variant="contained"
                  size="large"
                  color="primary"
                  fullWidth
                  className={classes.button}
                  style={{ marginTop: "5px" }}
                >
                  Sign In
                </Button>
              </Tooltip>
            </Link>

            <br />
            <br />
            <br />
            <br />
            <br />
          </Paper>
        </Grid>
      </Grid>
    </div>
  );
}

Join.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(Join);
