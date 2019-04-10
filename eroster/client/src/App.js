import React from "react";
import { CssBaseline, withStyles } from "@material-ui/core";
import { Switch, Route } from "react-router-dom";
//import Header from "./components/Layout/Header";
import JoinHeader from "./components/Layout/JoinHeader";
import Join from "./components/Authentication/Join";
import SignIn from "./components/Authentication/SignIn";

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
    <JoinHeader />
    {/* ['#F0F0F0','#F5F5F5','#F8F8F8','#F5F5F5']  */}
    <main className={classes.main} style={{ background: "#F5F5F5" }}>
      <br />
      <br />
      <br />
      <Switch>
        <Route path="/join" component={Join} />
        <Route path="/signin" component={SignIn} />
      </Switch>
    </main>
  </React.Fragment>
);

export default withStyles(styles)(App);
