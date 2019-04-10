import React from "react";
import { CssBaseline, withStyles } from "@material-ui/core";
import { Switch, Route } from "react-router-dom";

import SignIn from "./components/Authentication/SignIn";
import SignUp from "./components/Authentication/SignUp";

import Agency from "./components/Agency/Agency";

import Dashboard from "./components/Dashboard/Dashboard";
const styles = theme => ({});

const App = ({ classes }) => (
  <React.Fragment>
    <CssBaseline />

    {/* ['#F0F0F0','#F5F5F5','#F8F8F8','#F5F5F5']  */}
    <main className={classes.main} style={{ background: "#F5F5F5" }}>
      <Switch>
        <Route path="/agency" component={Agency} />
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/signup" component={SignUp} />
        <Route path="/" component={SignIn} />

        <Route path="/consultant" />
      </Switch>
    </main>
  </React.Fragment>
);

export default withStyles(styles)(App);
