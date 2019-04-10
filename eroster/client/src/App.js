import React from "react";
import { CssBaseline, withStyles } from "@material-ui/core";
import { Switch, Route } from "react-router-dom";

import SignIn from "./components/Authentication/SignIn";
import SignUp from "./components/Authentication/SignUp";

import Dashboard from "./components/Dashboard/Dashboard";
const styles = theme => ({
  main: {
    padding: 3 * theme.spacing.unit,
    [theme.breakpoints.down("xs")]: {
      padding: 2 * theme.spacing.unit
    }
  }
});

const App = ({ classes }) => (
  <React.Fragment>
    <CssBaseline />

    {/* ['#F0F0F0','#F5F5F5','#F8F8F8','#F5F5F5']  */}
    <main className={classes.main} style={{ background: "#F5F5F5" }}>
      <br />
      <br />
      <br />
      <Switch>
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/signup" component={SignUp} />
        <Route path="/" component={SignIn} />
      </Switch>
    </main>
  </React.Fragment>
);

export default withStyles(styles)(App);
