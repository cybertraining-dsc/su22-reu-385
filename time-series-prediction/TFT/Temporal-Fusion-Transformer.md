## Temporal Fusion Transformer(TFT)

TFT is an attention-based Deep Neural Network that has been 
optimized for performance and interpretability.

### TFT Time Series Prediction

Multi-horizon forecasting problems frequently contain a complex 
mix of inputs, including static (i.e. time-invariant) covariances,
known future inputs, and other exogenous time series that can only 
be observed historically, with no prior knowledge of how they 
interact with the target. While several deep learning models for 
multistep prediction have been proposed, they typically consist of 
black-box models that do not account for the full range of inputs
present in common scenarios. In this paper, we introduce the Temporal
Fusion Transformer (TFT), a novel attention-based architecture that 
combines high-performance multi-horizon forecasting with interpretable 
insights into temporal dynamics. The TFT employs recurrent layers for 
local processing and interpretable self-attention layers for learning 
long-term dependencies to learn temporal relationships at various scales.
The TFT also makes use of specialized components for the

``` python
```