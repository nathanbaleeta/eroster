import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";

import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";

import Highcharts from "highcharts";
import HighchartsReact from "highcharts-react-official";

const options = {
  credits: {
    enabled: false
  },
  chart: {
    type: "column"
  },
  title: {
    text: "Summary Statistics"
  },
  xAxis: {
    categories: ["Criteria"]
  },
  yAxis: {
    label: "Raters"
  },
  series: [
    {
      name: "C4D",
      data: [5.23]
    },
    {
      name: "Education",
      data: [6.23]
    },
    {
      name: "Health",
      data: [7.45]
    },
    {
      name: "M & E",
      data: [7.84]
    },
    {
      name: "Nutrition",
      data: [4.85]
    },
    {
      name: "WASH",
      data: [8.23]
    },
    {
      name: "ICT",
      data: [1.85]
    },
    {
      name: "HR",
      data: [9.23]
    }
  ]
};

const styles = theme => ({
  bigAvatar: {
    margin: 10,
    width: 160,
    height: 160,
    border: "3px solid black"
  },
  media: {
    height: 140
  },
  margin: {
    margin: theme.spacing.unit * 3
  },
  padding: {
    padding: `0 ${theme.spacing.unit * 2}px`
  },
  avatar: {
    margin: 10
  }
});

function SummaryStastics(props) {
  const { classes } = props;

  return (
    <div className={classes.root}>
      <Card className={classes.card}>
        <CardActionArea>
          <HighchartsReact highcharts={Highcharts} options={options} />
        </CardActionArea>
      </Card>
    </div>
  );
}

SummaryStastics.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(SummaryStastics);
