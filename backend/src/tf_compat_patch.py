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

except ImportError as e:
    # If tensorflow-probability is not available, create a more complete mock
    # This is a fallback that at least provides the basic structure
    import warnings
    warnings.warn(f"tensorflow-probability not found, using compatibility mock: {e}")

    if not hasattr(tf, 'contrib'):
        class ContribModule:
            pass
        tf.contrib = ContribModule()

    # Create a more complete mock for distributions that provides common classes
    class MockDistributions:
        # Common distribution classes that might be needed
        class Distribution:
            pass

        class Normal:
            pass

        class MultivariateNormalDiag:  # This was the missing attribute
            pass

        class Bernoulli:
            pass

        class Categorical:
            pass

        class Beta:
            pass

        class Dirichlet:
            pass

        class Exponential:
            pass

        class Gamma:
            pass

        class Laplace:
            pass

        class StudentT:
            pass

        class Uniform:
            pass

        # Add any other common distribution classes as needed
        pass

    tf.contrib.distributions = MockDistributions