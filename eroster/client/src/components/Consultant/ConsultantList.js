import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Avatar from "@material-ui/core/Avatar";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import IconButton from "@material-ui/core/IconButton";
import MoreVertIcon from "@material-ui/icons/MoreVert";

const styles = theme => ({
  root: {
    padding: theme.spacing.unit * 2
  },
  avatar: {},
  bigAvatar: {
    width: 100,
    height: 100
  }
});

function ConsultantList(props) {
  const { classes } = props;

  return (
    <div className={classes.root}>
      <Typography variant="h5" component="h3" color="default" align="center">
        Consultants
      </Typography>
      <br />
      <Grid container spacing={24}>
        <Grid item xs={6} sm={6}>
          <Card className={classes.card}>
            <CardHeader
              avatar={
                <Avatar
                  alt="Remy Sharp"
                  src="/static/images/avatar/1.jpg"
                  className={classes.bigAvatar}
                />
              }
              action={
                <IconButton>
                  <MoreVertIcon />
                </IconButton>
              }
              title="Nathan Baleeta"
              subheader="Technology for Development"
            />
          </Card>
        </Grid>
        <Grid item xs={6} sm={6}>
          <Card className={classes.card}>
            <CardHeader
              avatar={
                <Avatar
                  alt="Remy Sharp"
                  src="/static/images/avatar/2.jpg"
                  className={classes.bigAvatar}
                />
              }
              action={
                <IconButton>
                  <MoreVertIcon />
                </IconButton>
              }
              title="Peter Smith"
              subheader="C4D"
            />
          </Card>
        </Grid>
        <br />
        <Grid item xs={6} sm={6}>
          <Card className={classes.card}>
            <CardHeader
              avatar={
                <Avatar
                  alt="Remy Sharp"
                  src="/static/images/avatar/4.jpg"
                  className={classes.bigAvatar}
                />
              }
              action={
                <IconButton>
                  <MoreVertIcon />
                </IconButton>
              }
              title="Simon Lenox"
              subheader="September 14, 2016"
            />
          </Card>
        </Grid>
        <Grid item xs={6} sm={6}>
          <Card className={classes.card}>
            <CardHeader
              avatar={
                <Avatar
                  alt="Remy Sharp"
                  src="/static/images/avatar/10.jpeg"
                  className={classes.bigAvatar}
                />
              }
              action={
                <IconButton>
                  <MoreVertIcon />
                </IconButton>
              }
              title="Rosa Anita"
              subheader="Supply & Logistics"
            />
          </Card>
        </Grid>
        <Grid item xs={6} sm={6} />
      </Grid>
    </div>
  );
}

ConsultantList.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(ConsultantList);
