# Retail Data Cost Analysis Pipeline

This repository showcases a retail cost analysis pipeline built around the UCI Online Retail dataset. It combines Python data processing with interactive Tableau dashboards to provide end-to-end insights into product and vendor cost metrics.

## Project Structure

* **process\_retail\_data.py**
  A Python script that:

  1. Loads and cleans the raw `Online_Retail.xlsx` dataset.
  2. Standardizes records and handles missing or inconsistent entries.
  3. Calculates key cost metrics (e.g., calculated “should‑cost” vs. vendor quotes).
  4. Outputs the transformed data as `Processed_Retail_Data.csv`.

* **Online\_Retail.xlsx**
  The original UCI Online Retail transactions dataset, containing order-level details for product purchases.

* **Processed\_Retail\_Data.csv**
  The cleaned and enriched CSV featuring aggregated cost calculations and data quality flags.

* **tableau\_dashboard/**

  * `MyTableauDashboard.twbx` – a packaged Tableau workbook with interactive cost-analysis dashboards.
  * `preview.png` – a static snapshot of the primary dashboard view.

## Live Dashboard Embed

<div class='tableauPlaceholder' id='viz1746687355413' style='position: relative'>
  <noscript>
    <a href='#'>
      <img alt='Dashboard 1 ' src='https://public.tableau.com/static/images/P4/P4Y3GK6ZP/1_rss.png' style='border: none' />
    </a>
  </noscript>
  <object class='tableauViz'  style='display:none;'>
    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
    <param name='embed_code_version' value='3' />
    <param name='path' value='shared%2FP4Y3GK6ZP' />
    <param name='toolbar' value='yes' />
    <param name='static_image' value='https://public.tableau.com/static/images/P4/P4Y3GK6ZP/1.png' />
    <param name='animate_transition' value='yes' />
    <param name='display_static_image' value='yes' />
    <param name='display_spinner' value='yes' />
    <param name='display_overlay' value='yes' />
    <param name='display_count' value='yes' />
    <param name='language' value='en-US' />
  </object>
</div>
<script type='text/javascript'>
  var divElement = document.getElementById('viz1746687355413');
  var vizElement = divElement.getElementsByTagName('object')[0];
  if ( divElement.offsetWidth > 800 ) {
    vizElement.style.width='1087px'; vizElement.style.height='698px';
  } else if ( divElement.offsetWidth > 500 ) {
    vizElement.style.width='1087px'; vizElement.style.height='698px';
  } else {
    vizElement.style.width='100%'; vizElement.style.height='877px';
  }
  var scriptElement = document.createElement('script');
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

## Summary

A reproducible, version-controlled pipeline that:

1. **Cleans and transforms** raw retail transaction data using Python.
2. **Calculates actionable cost insights**, comparing vendor quotes against modeled should‑costs.
3. **Visualizes** results in an interactive Tableau dashboard embedded above.

This combination of data engineering, cost analysis, and dashboard development demonstrates core competencies for a Product Cost Associate and related analytical roles in retail and procurement.