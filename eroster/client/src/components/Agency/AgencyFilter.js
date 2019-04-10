import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import MenuItem from "@material-ui/core/MenuItem";

const styles = theme => ({
  root: {
    ...theme.mixins.gutters(),
    paddingTop: theme.spacing.unit * 2,
    paddingBottom: theme.spacing.unit * 2
  }
});

const advanceTypes = [
  {
    value: "1",
    label: "1"
  },
  {
    value: "2",
    label: "2"
  }
];

const commodities = [
  {
    value: "1",
    label: "1"
  },
  {
    value: "2",
    label: "2"
  },
  {
    value: "3",
    label: "3"
  },
  {
    value: "4",
    label: "4"
  }
];

const paymentModes = [
  {
    value: "1",
    label: "1"
  },
  {
    value: "2",
    label: "2"
  }
];
function AgencyFilter(props) {
  const { classes } = props;

  return (
    <div>
      <Paper className={classes.root} elevation={1}>
        <form>
          <Grid container spacing={24}>
            <Grid item xs={12} sm={12}>
              <Typography variant="headline" align="left" color="inherit">
                Filter by:
              </Typography>
            </Grid>

            <Grid item xs={12} sm={12}>
              <TextField
                id="advanceType"
                select
                name="advanceType"
                //value={this.state.advanceType}
                //onChange={event => this.handleActivation(event)}
                label="Country*"
                fullWidth
                helperText="Please select country"
                InputLabelProps={{
                  shrink: true
                }}
              >
                {advanceTypes.map(option => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>

            <Grid item xs={6} sm={6}>
              <TextField
                id="commodityAdvanced"
                //disabled={this.state.commodity}
                select
                name="commodityAdvanced"
                //value={this.state.commodityAdvanced}
                //onChange={this.onChange}
                label="Region"
                fullWidth
                helperText="Please select region"
                InputLabelProps={{
                  shrink: true
                }}
              >
                {commodities.map(option => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid item xs={6} sm={6}>
              <TextField
                id="paymentMode"
                select
                name="paymentMode"
                //value={this.state.paymentMode}
                //onChange={this.onChange}
                label="Sector"
                fullWidth
                helperText="Please select sector"
                InputLabelProps={{
                  shrink: true
                }}
              >
                {paymentModes.map(option => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>

            <Grid item xs={12} sm={12}>
              <TextField
                id="advanceType"
                select
                name="advanceType"
                //value={this.state.advanceType}
                //onChange={event => this.handleActivation(event)}
                label="Area of specialization*"
                fullWidth
                helperText="Please select expertise"
                InputLabelProps={{
                  shrink: true
                }}
              >
                {advanceTypes.map(option => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>

            <Grid item xs={12} sm={12}>
              <br />
              <br />

              <Button
                type="submit"
                variant="contained"
                size="large"
                color="secondary"
                fullWidth
              >
                Search
              </Button>
            </Grid>
          </Grid>
        </form>
      </Paper>
    </div>
  );
}

AgencyFilter.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(AgencyFilter);
