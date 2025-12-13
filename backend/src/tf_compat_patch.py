"""
TensorFlow compatibility patch to handle deprecated tf.contrib.distributions import.
This module should be imported before any modules that use tf.contrib.distributions.
"""
import sys
import tensorflow as tf

# Check if tensorflow-probability is available
try:
    import tensorflow_probability as tfp
    # Create a compatibility layer for tf.contrib.distributions
    if not hasattr(tf, 'contrib'):
        class ContribModule:
            pass
        tf.contrib = ContribModule()

    if not hasattr(tf.contrib, 'distributions'):
        tf.contrib.distributions = tfp.distributions
except ImportError:
    # If tensorflow-probability is not available, try alternative approach
    # This is a fallback for cases where tfp is not available
    if not hasattr(tf, 'contrib'):
        class ContribModule:
            pass
        tf.contrib = ContribModule()

    # Create a mock for distributions if needed
    if not hasattr(tf.contrib, 'distributions'):
        class MockDistributions:
            pass
        tf.contrib.distributions = MockDistributions()