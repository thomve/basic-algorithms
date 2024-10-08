# Overview of Reinforcement Learning Algorithms
Reinforcement learning (RL) is a type of machine learning where an agent learns to make decisions by interacting with an environment and receiving rewards or penalties. There are several types of RL algorithms, broadly categorized based on how they approach learning.

## 1. Model-Free Algorithms
These algorithms do not require a model of the environment and can be further classified into **value-based** and **policy-based** methods.

### Value-Based Algorithms
- **Q-Learning**:
    - Off-policy algorithm that learns the value of actions for each state.
    - Equation: 
        $$Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$$
- **SARSA (State-Action-Reward-State-Action)**:
    - On-policy algorithm that updates the Q-values based on the actions the agent actually takes.
    - Equation: 
        $$Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma Q(s', a') - Q(s, a)]$$
- **Deep Q-Networks (DQN)**:
    - Extension of Q-learning using deep neural networks to approximate Q-values in high-dimensional spaces.

### Policy-Based Algorithms
- **REINFORCE**:
    - Monte Carlo policy gradient algorithm that directly updates the policy based on the gradient of expected rewards.
    - Equation:
        $$\theta \leftarrow \theta + \alpha \nabla_\theta \log \pi_\theta(a|s) R$$
- **Actor-Critic Methods**:
    - Combines policy-based (actor) and value-based (critic) approaches. The actor updates the policy, and the critic evaluates the policy.
    - Example: **Advantage Actor-Critic (A2C)**, **Asynchronous Advantage Actor-Critic (A3C)**.

### Temporal Difference Learning
- **TD(0)**:
    - A hybrid of Monte Carlo and Dynamic Programming methods that updates the value function based on the difference between estimated and actual rewards.

## 2. Model-Based Algorithms
These algorithms involve building a model of the environment and using it for planning and simulation.

- **Dyna-Q**:
    - Combines model-free Q-learning and planning. The agent learns from both real and simulated experiences generated by a model of the environment.
    
- **Model Predictive Control (MPC)**:
    - Uses a model to plan future actions by optimizing over a time horizon.

## 3. Policy Gradient-Based Algorithms
These algorithms explicitly optimize the policy by adjusting parameters in the direction of better performance.

- **Proximal Policy Optimization (PPO)**:
    - Ensures stable learning by limiting large policy updates using a clipped objective function.
    - Equation:
        $$L(\theta) = \min(r(\theta) \hat{A}, \text{clip}(r(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A})$$
    
- **Trust Region Policy Optimization (TRPO)**:
    - Limits how much the policy is allowed to change between updates by enforcing a trust region for stable learning.
    
- **Soft Actor-Critic (SAC)**:
    - Maximizes both the expected reward and the entropy of the policy, encouraging exploration by reducing policy determinism.

## 4. Evolutionary Algorithms
These methods evolve policies using evolutionary strategies inspired by biological evolution.

- **Evolution Strategies (ES)**:
    - Optimizes policies by sampling and evolving them based on performance (mutation and selection).

## 5. Multi-Agent Reinforcement Learning (MARL)
Multiple agents interact within the same environment and learn either cooperatively or competitively.

- **Independent Q-Learning**:
    - Each agent learns its own Q-values independently in a shared environment.
    
- **MADDPG (Multi-Agent Deep Deterministic Policy Gradient)**:
    - Extension of DDPG for multi-agent environments where each agent learns its own policy and critic, with access to global observations.

## 6. Distributional RL
Models the distribution of future rewards instead of only their expected value.

- **Categorical DQN**:
    - Approximates the distribution of Q-values instead of just their expected values.
    
- **Quantile Regression DQN (QR-DQN)**:
    - Learns the quantiles of the return distribution.

## 7. Hierarchical RL
In hierarchical RL, the agent learns at multiple levels of abstraction.

- **Options Framework**:
    - The agent learns a higher-level policy that selects from a set of lower-level "options" or sub-policies.
    
- **H-DQN (Hierarchical Deep Q-Networks)**:
    - A hierarchical version of DQN where the high-level policy chooses goals, and the low-level policy works to achieve them.

## 8. Off-Policy vs. On-Policy
- **On-Policy**:
    - The policy is learned based on the actions the agent actually takes (e.g., SARSA, A2C).
    
- **Off-Policy**:
    - The agent learns a policy different from the one generating the data (e.g., Q-learning, DQN, DDPG).

## 9. Continuous Action Space Algorithms
These methods work in environments with continuous action spaces.

- **Deep Deterministic Policy Gradient (DDPG)**:
    - Off-policy algorithm for continuous action spaces that combines policy gradients with actor-critic methods.
    
- **Twin Delayed DDPG (TD3)**:
    - Variant of DDPG that reduces overestimation bias by using two critics and delaying the policy updates.

---
